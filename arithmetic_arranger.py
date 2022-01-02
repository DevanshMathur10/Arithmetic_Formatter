def arithmetic_arranger(problems,solns=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  l1=""
  l2=""
  l3=""
  l4=""

  for i,prob in enumerate(problems):
    num1,op,num2=prob.split()

    if op not in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."

    if not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits."

    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."

    if op == "+":
      soln = int(num1) + int(num2)
    else:
      soln = int(num1) - int(num2)

    num_length = len(max([num1,num2], key=len))

    l1+=num1.rjust(num_length+2)
    l2+=op+num2.rjust(num_length+1)
    l3+="-"*(num_length+2)
    l4+=str(soln).rjust(num_length+2)

    if i < len(problems)-1:
      l1 += "    "
      l2 += "    "
      l3 += "    "
      l4 += "    "

  ques = l1 + "\n" + l2 + "\n" + l3

  if solns:
    ques += "\n" + l4
  return ques