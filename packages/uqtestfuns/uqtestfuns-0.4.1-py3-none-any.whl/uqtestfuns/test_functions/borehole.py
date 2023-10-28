"""
Module with an implementation of the Borehole function.

The Borehole test function [1] is an eight-dimensional scalar-valued function
that models water flow through a borehole that is drilled from
the ground surface through two aquifers.

The unit of the output is [m^3/year].

References
----------

1. W. V. Harper and S. K. Gupta, “Sensitivity/Uncertainty Analysis of
   a Borehole Scenario Comparing Latin Hypercube Sampling and
   Deterministic Sensitivity Approaches”, Office of Nuclear Waste
   Isolation, Battelle Memorial Institute, Columbus, Ohio,
   BMI/ONWI-516, 1983.
   URL: https://inldigitallibrary.inl.gov/PRR/84393.pdf
2. Max D. Morris, T. J. Mitchell, and D. Ylvisaker, “Bayesian design and
   analysis of computer experiments: Use of derivatives in surface
   prediction,” Technometrics, vol. 35, no. 3, pp. 243–255, 1993.
   DOI: 10.1080/00401706.1993.10485320
"""
import numpy as np

from ..core.uqtestfun_abc import UQTestFunABC
from ..core.prob_input.input_spec import UnivDistSpec, ProbInputSpecFixDim

__all__ = ["Borehole"]

# From Ref. [1]
INPUT_MARGINALS_HARPER1983 = [
    UnivDistSpec(
        name="rw",
        distribution="normal",
        parameters=[0.10, 0.0161812],
        description="radius of the borehole [m]",
    ),
    UnivDistSpec(
        name="r",
        distribution="lognormal",
        parameters=[7.71, 1.0056],
        description="radius of influence [m]",
    ),
    UnivDistSpec(
        name="Tu",
        distribution="uniform",
        parameters=[63070.0, 115600.0],
        description="transmissivity of upper aquifer [m^2/year]",
    ),
    UnivDistSpec(
        name="Hu",
        distribution="uniform",
        parameters=[990.0, 1100.0],
        description="potentiometric head of upper aquifer [m]",
    ),
    UnivDistSpec(
        name="Tl",
        distribution="uniform",
        parameters=[63.1, 116.0],
        description="transmissivity of lower aquifer [m^2/year]",
    ),
    UnivDistSpec(
        name="Hl",
        distribution="uniform",
        parameters=[700.0, 820.0],
        description="potentiometric head of lower aquifer [m]",
    ),
    UnivDistSpec(
        name="L",
        distribution="uniform",
        parameters=[1120.0, 1680.0],
        description="length of the borehole [m]",
    ),
    UnivDistSpec(
        name="Kw",
        distribution="uniform",
        parameters=[9985.0, 12045.0],
        description="hydraulic conductivity of the borehole [m/year]",
    ),
]

# From Ref. [2]
INPUT_MARGINALS_MORRIS1993 = list(INPUT_MARGINALS_HARPER1983)
INPUT_MARGINALS_MORRIS1993[0:2] = [
    UnivDistSpec(
        name="rw",
        distribution="uniform",
        parameters=[0.05, 0.15],
        description="radius of the borehole [m]",
    ),
    UnivDistSpec(
        name="r",
        distribution="uniform",
        parameters=[100, 50000],
        description="radius of influence [m]",
    ),
]

AVAILABLE_INPUT_SPECS = {
    "Harper1983": ProbInputSpecFixDim(
        name="Borehole-Harper-1983",
        description=(
            "Probabilistic input model of the Borehole model "
            "from Harper and Gupta (1983)."
        ),
        marginals=INPUT_MARGINALS_HARPER1983,
        copulas=None,
    ),
    "Morris1993": ProbInputSpecFixDim(
        name="Borehole-Morris-1993",
        description=(
            "Probabilistic input model of the Borehole model "
            "from Morris et al. (1993)."
        ),
        marginals=INPUT_MARGINALS_MORRIS1993,
        copulas=None,
    ),
}

DEFAULT_INPUT_SELECTION = "Harper1983"


def evaluate(xx: np.ndarray) -> np.ndarray:
    """Evaluate the Borehole function on a set of input values.

    Parameters
    ----------
    xx : np.ndarray
        8-Dimensional input values given by N-by-8 arrays where
        N is the number of input values.

    Returns
    -------
    np.ndarray
        The output of the Borehole function evaluated on the input values.
        The output is a 1-dimensional array of length N.
    """
    # Compute the Borehole function
    nom = 2 * np.pi * xx[:, 2] * (xx[:, 3] - xx[:, 5])
    denom_1 = np.log(xx[:, 1] / xx[:, 0])
    denom_2 = (
        2
        * xx[:, 6]
        * xx[:, 2]
        / (np.log(xx[:, 1] / xx[:, 0]) * xx[:, 0] ** 2 * xx[:, 7])
    )
    denom_3 = xx[:, 2] / xx[:, 4]

    yy = nom / (denom_1 * (1 + denom_2 + denom_3))

    return yy


class Borehole(UQTestFunABC):
    """A concrete implementation of the Borehole function."""

    _tags = ["metamodeling", "sensitivity"]
    _description = "Borehole function from Harper and Gupta (1983)"
    _available_inputs = AVAILABLE_INPUT_SPECS
    _available_parameters = None
    _default_input = DEFAULT_INPUT_SELECTION
    _default_spatial_dimension = 8

    eval_ = staticmethod(evaluate)
