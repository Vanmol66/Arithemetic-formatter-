def arithmetic_formatter(problems, show_answers):#main function of the code 
    if len(problems) > 5:
        return 'Error: Too many problems.' #can't work for more than 4 problems at time
    
    top = []#take top line of equation as empty list
    down= []#take bottom line of equation as empty list
    dashes = []#take a empty list to for dashes to seperate equation
    answers = []#takes answers as a empty list for now
    
    for problem in problems:
        parts = problem.split()
        if parts[1] not in ['+', '-']:#value at index 1 must be a operator of type subtraction or addition
            return "Error: Operator must be '+' or '-'."
        
        if not (parts[0].isdigit() and parts[2].isdigit()):#values at index 0 and 2 must we digits to perform the operation
            return 'Error: Numbers must only contain digits.'
        
        if len(parts[0]) > 4 or len(parts[2]) > 4: #values at index 0 or 2 must be less than of length 4  
            return 'Error: Numbers cannot be more than four digits.'
        
        width = max(len(parts[0]), len(parts[2])) + 2 #this makes the space for the max length of the equation 
        top.append(parts[0].rjust(width))#update the value at index 0 at the top line of equation
        down.append(parts[1] + parts[2].rjust(width - 1))# update the value at index 1 which is a operator and value at index 2 in second line
        dashes.append('-' * width)#makes a dash line of max length for sepration
        
        if show_answers:
            result = str(eval(problem)) #store the each problem as a string
            answers.append(result.rjust(width))#append the result acc. to width
    
    arranged_problems = (
        '    '.join(top) + "\n" + #presents the final output in formatted manner
        '    '.join(down) + "\n" +
        '    '.join(dashes)
    )
    
    if show_answers:
        arranged_problems += "\n" + '    '.join(answers) # gives out the final result/answer of the problem
    
    return arranged_problems
    
print(arithmetic_formatter(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)) #exapmle of the type of problems this source code will resolve