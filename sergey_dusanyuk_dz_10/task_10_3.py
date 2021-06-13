
class SubError(Exception):
    def __str__(self):
        return 'ERROR: incorrect sub operation'


class OrganicCell:
    def __init__(self, cell_amount: int):
        self.cell_amount = cell_amount

    def __add__(self, other):
        return OrganicCell(self.cell_amount + other.cell_amount)

    def __sub__(self, other):
        if self.cell_amount > other.cell_amount:
            return OrganicCell(self.cell_amount - other.cell_amount)
        else:
            raise SubError

    def __mul__(self, other):
        return OrganicCell(self.cell_amount * other.cell_amount)

    def __floordiv__(self, other):
        return OrganicCell(self.cell_amount // other.cell_amount)

    def __truediv__(self, other):
        return OrganicCell(self.cell_amount / other.cell_amount)

    def make_order(self, cell_in_row):
        full_rows = self.cell_amount // cell_in_row
        last_row_cells = self.cell_amount % cell_in_row
        full_row = ''.join(['*' for i in range(cell_in_row)])
        last_row = ''.join(['*' for i in range(last_row_cells)])
        rows = [full_row for i in range(full_rows)]
        rows.append(last_row)
        rows = '\n'.join(rows)
        return rows


if __name__ == '__main__':
    o1 = OrganicCell(5)
    o2 = OrganicCell(4)

    o_add = o1 + o2
    print(o_add.cell_amount)

    o_sub = o1 - o2
    print(o_sub.cell_amount)

    try:
        o_sub_1 = o2 - o1
    except SubError as e:
        print(e)

    o_mul = o1 * o2
    print(o_mul.cell_amount)

    o_floordiv = o1 // o2
    print(o_floordiv.cell_amount)

    o_truediv = o1 / o2
    print(o_truediv.cell_amount)

    print('o1.make_order(2)')
    print(o1.make_order(2))

    print('o1.make_order(6)')
    print(o1.make_order(6))

    print('o_mul.make_order(7)')
    print(o_mul.make_order(7))
