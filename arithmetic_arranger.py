def arithmetic_arranger(problems, show_answer=False):
  if len(problems) > 5:
      return "Error: Too many problems."

  arranged_problems = {
      "first_line": "",
      "second_line": "",
      "dash_line": "",
      "answer_line": ""
  }

  for problem in problems:
      operand1, operator, operand2 = problem.split()
      if operator not in ['+', '-']:
          return "Error: Operator must be '+' or '-'."
      if not operand1.isdigit() or not operand2.isdigit():
          return "Error: Numbers must only contain digits."
      if len(operand1) > 4 or len(operand2) > 4:
          return "Error: Numbers cannot be more than four digits."

      width = max(len(operand1), len(operand2)) + 2
      arranged_problems["first_line"] += operand1.rjust(width) + "    "
      arranged_problems["second_line"] += operator + " " + operand2.rjust(width - 2) + "    "
      arranged_problems["dash_line"] += "-" * width + "    "

      if show_answer:
          if operator == '+':
              answer = str(int(operand1) + int(operand2))
          else:
              answer = str(int(operand1) - int(operand2))

          arranged_problems["answer_line"] += answer.rjust(width) + "    "

  arranged_output = (
      arranged_problems["first_line"].rstrip() + "\n" +
      arranged_problems["second_line"].rstrip() + "\n" +
      arranged_problems["dash_line"].rstrip()
  )

  if show_answer:
      arranged_output += "\n" + arranged_problems["answer_line"].rstrip()

  return arranged_output
