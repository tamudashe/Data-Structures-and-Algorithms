"""
Given a rod of length n inches and a table of prices pi for i D 1; 2; : : : ; n, determine the maximum revenue rn
obtain able by cutting up the rod and selling the pieces. Note that if the price pn for a rod of length n is large
enough,an optimal solution may require no cutting at all.
"""


def max_revenue(rod, price_chart):
    pass


def main():
    price_chart = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}
    rod = 4
    print(max_revenue(rod, price_chart))


if __name__ == '__main__':
    main()
