name = "x"

def get_problem(self, difficulty):
    x = self.generate_number(difficulty)
    y = self.generate_number(difficulty)
    question = "%s x %s" % (x, y)
    answer = x * y
    return question, answer