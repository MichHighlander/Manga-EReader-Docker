class Utils:
    @staticmethod
    def calculate_total_int_from_list(int_list: list)->int:
        total = 0
        for item in int_list:
            total = total + item
        return total
    
    