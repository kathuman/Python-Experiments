"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from thinkbayes import Suite
import thinkplot


class Dice(Suite):
    """Represents hypotheses about which die was rolled."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: integer number of sides on the die
        data: integer die roll
        """
        if hypo < data:
            return 0
        else:
            return 1.0/hypo

class Train(Dice):
    """Represents hypotheses about how many trains the company has.

    The likelihood function for the train problem is the same as
    for the Dice problem.
    """


def main():
    hypos = xrange(1, 1001)
    suite = Train(hypos)

    suite.Update(60)
    print(suite.Mean())

    thinkplot.PrePlot(1)
    thinkplot.Pmf(suite)
    thinkplot.Save(root='train1',
                   xlabel='Number of trains',
                   ylabel='Probability',
                   formats=['pdf', 'eps'])


if __name__ == '__main__':
    main()