# Case Study — Using Prompt Engineering to Debug Python Code

## Introduction
The goal of this task was to use prompt engineering to identify issues in a buggy Python script and generate an improved version. This case study documents the prompt chain, the AI-generated reasoning, and the final result.

## Problem
The original script produced incorrect output due to logical mistakes and missing validation.  
Key issues included:
- Using len(num) instead of len(numbers)
- No input validation
- No handling for empty lists

## Prompting Process
The debugging process was completed using a three-prompt chain:
1. Ask the model to identify all issues in the code  
2. Ask for a corrected and improved version  
3. Ask for a simple explanation comparing both versions  

The model provided structured reasoning and a clean rewrite of the function.

## Result
The corrected script:
- Validates input  
- Prevents runtime errors  
- Is easier to read  
- Produces correct output  

The final version also uses sum(), improving readability and reducing code length.

## Conclusion
Prompt engineering helped break the debugging task into clear steps.  
The prompts produced detailed explanations, a corrected script, and an improved structure.  
This approach is effective for learning, debugging, and refining Python code quickly.
