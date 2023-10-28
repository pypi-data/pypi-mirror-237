# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Two-qubit gate decomposition."""
# pylint: disable=invalid-name
from math import pi, sqrt

import numpy as np
from scipy import linalg

from mindquantum.core import gates
from mindquantum.core.circuit import Circuit
from mindquantum.core.gates import QuantumGate

from .. import utils
from ..fixed_decompose import crx_decompose, cry_decompose, crz_decompose
from ..utils import (
    M_DAG,
    A,
    M,
    is_tensor_prod,
    kron_decomp,
    kron_factor_4x4_to_2x2s,
    optimize_circuit,
    params_abc,
    params_u3,
    params_zyz,
)


def tensor_product_decompose(gate: QuantumGate, return_u3: bool = True) -> Circuit:
    """
    Tensor product decomposition of a 2-qubit gate.

    Args:
        gate (:class:`~.core.gates.QuantumGate`): 2-qubit gate composed by tensor product.
        return_u3 (bool): return gates in form of :class:`~.core.gates.U3` if ``True``, otherwise
            return :class:`~.core.gates.UnivMathGate`. Default: ``True``.

    Returns:
        :class:`~.core.circuit.Circuit`, including two single-qubit gates.

    Examples:
        >>> import mindquantum as mq
        >>> from mindquantum.algorithm.compiler.decompose import tensor_product_decompose
        >>> g = mq.UnivMathGate('XY', np.kron(mq.X.matrix(), mq.Y.matrix())).on([0, 1])
        >>> print(mq.Circuit() + g)
        q0: ──XY──
              │
        q1: ──XY──
        >>> circ_decomposed = tensor_product_decompose(g)
        >>> print(circ_decomposed)
        q0: ──U3(𝜃=π, 𝜑=-π/2, 𝜆=π/2)──

        q1: ────U3(𝜃=π, 𝜑=0, 𝜆=0)─────
    """
    if len(gate.obj_qubits) != 2 or gate.ctrl_qubits:
        raise ValueError(f'{gate} is not a 2-qubit gate with designated qubits')
    if not is_tensor_prod(gate.matrix()):
        raise ValueError(f'{gate} is not a tensor-product unitary gate.')
    u0, u1 = kron_decomp(gate.matrix())
    circ = Circuit()
    if return_u3:
        circ += gates.U3(*params_u3(u0)).on(gate.obj_qubits[0])  # pylint: disable=no-value-for-parameter
        circ += gates.U3(*params_u3(u1)).on(gate.obj_qubits[1])  # pylint: disable=no-value-for-parameter
    else:
        circ += gates.UnivMathGate('U0', u0).on(gate.obj_qubits[0])
        circ += gates.UnivMathGate('U1', u1).on(gate.obj_qubits[1])
    return optimize_circuit(circ)


def abc_decompose(gate: QuantumGate, return_u3: bool = True) -> Circuit:
    """
    Decompose two-qubit controlled gate via ABC decomposition.

    Args:
        gate (:class:`~.core.gates.QuantumGate`): quantum gate with 1 control bit and 1 target bit.
        return_u3 (bool): return gates in form of :class:`~.core.gates.U3` if ``True``, otherwise
            return :class:`~.core.gates.UnivMathGate`. Default: ``True``.

    Returns:
        :class:`~.core.circuit.Circuit`, including at most 2 CNOT gates and 4 single-qubit gates.

    Examples:
        >>> import mindquantum as mq
        >>> from mindquantum.algorithm.compiler.decompose import abc_decompose
        >>> from scipy.stats import unitary_group
        >>> g = mq.UnivMathGate('U', unitary_group.rvs(2, random_state=123)).on(1, 0)
        >>> print(mq.Circuit() + g)
        q0: ──●──
              │
        q1: ──U──
        >>> circ_decomposed = abc_decompose(g)
        >>> print(circ_decomposed)
        q0: ─────────────●───────────────────────────────●────────────RZ(1.15)─────────
                         │                               │
        q1: ──RZ(2.6)────X────U3(𝜃=1.1, 𝜑=π, 𝜆=-0.66)────X────U3(𝜃=1.1, 𝜑=-5.09, 𝜆=0)──
    """
    if len(gate.ctrl_qubits) != 1 or len(gate.obj_qubits) != 1:
        raise ValueError(f'{gate} is not a two-qubit controlled gate with designated qubits')
    if isinstance(gate, gates.RX):
        return crx_decompose(gate)[0]
    if isinstance(gate, gates.RY):
        return cry_decompose(gate)[0]
    if isinstance(gate, gates.RZ):
        return crz_decompose(gate)[0]

    cq = gate.ctrl_qubits[0]
    tq = gate.obj_qubits[0]
    _, (_, phi, lam) = params_zyz(gate.matrix())
    alpha, (a, b, c) = params_abc(gate.matrix())
    circ = Circuit()
    if return_u3:
        # regardless global phases
        circ += gates.RZ((lam - phi) / 2).on(tq)
        circ += gates.X.on(tq, cq)
        circ += gates.U3(*params_u3(b)).on(tq)  # pylint: disable=no-value-for-parameter
        circ += gates.X.on(tq, cq)
        circ += gates.U3(*params_u3(a)).on(tq)  # pylint: disable=no-value-for-parameter
        circ += gates.RZ(alpha).on(cq)
    else:
        circ += gates.UnivMathGate('C', c).on(tq)
        circ += gates.X.on(tq, cq)
        circ += gates.UnivMathGate('B', b).on(tq)
        circ += gates.X.on(tq, cq)
        circ += gates.UnivMathGate('A', a).on(tq)
        circ += gates.PhaseShift(alpha).on(cq)
    return optimize_circuit(circ)


# pylint: disable=too-many-locals
def kak_decompose(gate: QuantumGate, return_u3: bool = True) -> Circuit:
    r"""
    KAK decomposition (CNOT basis) of an arbitrary two-qubit gate.

    For more detail, please refer to `An Introduction to Cartan's KAK Decomposition for QC
    Programmers <https://arxiv.org/abs/quant-ph/0406176>`_.

    Args:
        gate (:class:`~.core.gates.QuantumGate`): 2-qubit quantum gate.
        return_u3 (bool): return gates in form of :class:`~.core.gates.U3` if ``True``, otherwise
            return :class:`~.core.gates.UnivMathGate`. Default: ``True``.

    Returns:
        :class:`~.core.circuit.Circuit`, including at most 3 CNOT gates and 6 single-qubit gates.

    Examples:
        >>> import mindquantum as mq
        >>> from mindquantum.algorithm.compiler.decompose import kak_decompose
        >>> from scipy.stats import unitary_group
        >>> g = mq.UnivMathGate('U', unitary_group.rvs(4, random_state=123)).on([0, 1])
        >>> print(mq.Circuit() + g)
        q0: ──U──
              │
        q1: ──U──
        >>> circ_decomposed = kak_decompose(g)
        >>> print(circ_decomposed)
        q0: ──U3(𝜃=0.88, 𝜑=0.46, 𝜆=-0.65)────●─────U3(𝜃=π/2, 𝜑=-0.26, 𝜆=-π)────●──>>
                                             │                                 │  >>
        q1: ───U3(𝜃=1.3, 𝜑=-0.22, 𝜆=-2.6)────X────U3(𝜃=0, 𝜑=-0.19, 𝜆=-0.19)────X──>>
        ////////////////////////////////////////////////////////////////////////////////
        q0: <<────U3(𝜃=π/2, 𝜑=0, 𝜆=π)──────●────U3(𝜃=2.27, 𝜑=-1.87, 𝜆=3.88)──
            <<                             │
        q1: <<──U3(𝜃=0, 𝜑=0.36, 𝜆=0.36)────X────U3(𝜃=2.73, 𝜑=1.86, 𝜆=-2.47)──
    """
    if len(gate.obj_qubits) != 2 or gate.ctrl_qubits:
        raise ValueError(f'{gate} is not an arbitrary 2-qubit gate with designated qubits')
    pauli_i = gates.I.matrix()
    pauli_x = gates.X.matrix()
    pauli_z = gates.Z.matrix()

    # construct a new matrix replacing U
    u_su4 = M_DAG @ utils.remove_glob_phase(gate.matrix()) @ M  # ensure the decomposed object is in SU(4)
    ur = np.real(u_su4)  # real part of u_su4
    ui = np.imag(u_su4)  # imagine part of u_su4

    # simultaneous SVD decomposition
    (q_left, q_right), (dr, di) = utils.simult_svd(ur, ui)
    d = dr + 1j * di

    _, a0, a1 = kron_factor_4x4_to_2x2s(M @ q_left @ M_DAG)
    _, b0, b1 = kron_factor_4x4_to_2x2s(M @ q_right.T @ M_DAG)

    k = linalg.inv(A) @ np.angle(np.diag(d))
    h1, h2, h3 = -k[1:]

    u0 = 1j / sqrt(2) * (pauli_x + pauli_z) @ linalg.expm(-1j * (h1 - pi / 4) * pauli_x)
    v0 = -1j / sqrt(2) * (pauli_x + pauli_z)
    u1 = linalg.expm(-1j * h3 * pauli_z)
    v1 = linalg.expm(1j * h2 * pauli_z)
    w = (pauli_i - 1j * pauli_x) / sqrt(2)

    # list of operators
    rots1 = [b0, u0, v0, a0 @ w]  # rotation gate on idx1
    rots2 = [b1, u1, v1, a1 @ w.conj().T]

    idx1, idx2 = gate.obj_qubits
    circ = Circuit()
    if return_u3:
        circ += gates.U3(*params_u3(rots1[0])).on(idx1)  # pylint: disable=no-value-for-parameter
        circ += gates.U3(*params_u3(rots2[0])).on(idx2)  # pylint: disable=no-value-for-parameter
        circ += gates.X.on(idx2, idx1)
        circ += gates.U3(*params_u3(rots1[1])).on(idx1)  # pylint: disable=no-value-for-parameter
        circ += gates.U3(*params_u3(rots2[1])).on(idx2)  # pylint: disable=no-value-for-parameter
        circ += gates.X.on(idx2, idx1)
        circ += gates.U3(*params_u3(rots1[2])).on(idx1)  # pylint: disable=no-value-for-parameter
        circ += gates.U3(*params_u3(rots2[2])).on(idx2)  # pylint: disable=no-value-for-parameter
        circ += gates.X.on(idx2, idx1)
        circ += gates.U3(*params_u3(rots1[3])).on(idx1)  # pylint: disable=no-value-for-parameter
        circ += gates.U3(*params_u3(rots2[3])).on(idx2)  # pylint: disable=no-value-for-parameter
    else:
        circ += gates.UnivMathGate('B0', rots1[0]).on(idx1)
        circ += gates.UnivMathGate('B1', rots2[0]).on(idx2)
        circ += gates.X.on(idx2, idx1)
        circ += gates.UnivMathGate('U0', rots1[1]).on(idx1)
        circ += gates.UnivMathGate('U1', rots2[1]).on(idx2)
        circ += gates.X.on(idx2, idx1)
        circ += gates.UnivMathGate('V0', rots1[2]).on(idx1)
        circ += gates.UnivMathGate('V1', rots2[2]).on(idx2)
        circ += gates.X.on(idx2, idx1)
        circ += gates.UnivMathGate('W0', rots1[3]).on(idx1)
        circ += gates.UnivMathGate('W1', rots2[3]).on(idx2)
    return optimize_circuit(circ)
