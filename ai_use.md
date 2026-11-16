# AI Use

Generative AI used: Yes / No (choose one)

If no group member used AI, no entries are needed. Otherwise add an entry for each substantive use, including assistance with code, design, debugging, documentation or videos.

## Entry

- Member and date: 11 November 2026
- Tool and model/version, where available: Copilot on VS code
- Purpose: Debugging, Clear_screen() function and get_key() function
- Relevant prompts and outputs used, or retained transcript location: 
1. "How to clear the screen before every new output, and how to make an input only read what key is pressed?" Output the clear_screen() function and the get_key() function
2. "Can you debug the code for any bugs?" Output: suggestions on game design, but no errors given.
- Files/materials affected: 
clear_screen() function and get_key() function added to the main game file.
- What we kept, changed or rejected: Kept the two functions, and rejected the debug suggestions for how the game should run. the clear_screen() function used cls and clear, but we changed it to ANSI code because clear only gives scrollback for mac OS.
- How we checked it; tests and corrections: Using a separate testing file, we tested the clear_screen() and get_key() function so they worked properly before adding it to the main game. Found out that clear only does scrollback on mac, so we changed it.

Keep evidence accessible to the teaching team. Remove credentials and unrelated personal information. Submit the completed file as `ai_use.md` with the project.