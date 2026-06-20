# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
	+ the difficulty is already set to Normal, the left side has the Settings pane
	+ There is drop-down caret for "Develop Debug Info", where the Secret is the number to guess, also remaining attemps, SCore (unknown mechanism), Difficulty, and History (list) with square bracket
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
   + "New Game" button didn't work well
   + "Submit Guess" button doesn't reset input

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Click "Submit Guess" with number typed in when "Developer Debug Info" open|Clears field and process input|doesn't clear field and processess input on second | none|
| Click "New Game"| the game should reset, history should clear, should clear the "Enter your guess:" area | the history stays, no numbers | none |
| Entered a guess that is higher than the Secret| should get a response to go Lower | tells me to Go Higher! | none |
| Hard difficulty| the Range should be wider than Normal difficulty| the range is less than Normal difficulty | none |
| Easy difficulty| the Attempts allowed should be higher than Normal difficulty | the Attempts allowed is less than Normal difficulty
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
	+ (My Answer) Claude Code enterprise edition was used 
		* mostly Haiku + Sonnet with Med-High Effort

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
	+ (My Answer) The process of refactoring, asking CC to address each of the four NotImplementedError() raised alerts, it moved the code section including any other code changes for earlier bug fixes. 
		* Verified by looking at the code to see it moved, then running the app with streamlit, and seeing the behavior remain the same.


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
	+ (My Answer) When expanding the number of test cases, I prompted CC:
		* "can you provide more tests? specifically for edge cases not already covered"
		* The response included code change to use MagicMock(), this seems overly complicated to me so I stopped the code change and asked for tests without that package, then CC asked if I wanted to implement certain functions then I noticed there were more code to be added for logic_utils.py
		* After all the functions from app.py were refactored and moved out to logic_utils.py, I asked CC if writing 24 pytest was the right move instead of MagickMock() and said it was because no streamlit dependency

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  + (My Answer) I tested it in Streamlit and made sure the logic felt right and clicking certain buttons performed as expected for the app.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  + (My Answer) Writing test cases to check if a guess should respond with a win, response of too high/low, or invalid led to exploration of the code and seeing how the score is calculated, which was a mystery to me before.

- Did AI help you design or understand any tests? How?
  + (My Answer) Yes, I prompted AI to design the tests to make sure each difficulty was returning the correct range for what the secret guess is.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  + (My Answer) This contains the logic for how the app is restarted when the "New Game" button is pushed — the session state changes throughout a game but all its values are reset to pre-specified starting values.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  + (My Answer) Starting a new chat for each bug or goal to address — it helps keep the focus organized of certain work performed.

- What is one thing you would do differently next time you work with AI on a coding task?
  + (My Answer) Ask the AI to focus on certain sections of code rather than entire files at once.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  + (My Answer) AI will generate relevant code that is useful and solves issues when directed to the correct section of code and provided info in the prompt or spec about what the expected functionality is.
