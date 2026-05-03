To use the new DeepSeek-V4-Flash in [Ollama](https://ollama.com/library/deepseek-v4-flash), you primarily use the ollama run command in your terminal. Because this model is massive (~160 GB for local weights), it is most commonly used as a cloud-hosted model within the Ollama ecosystem to save local hardware resources. [1, 2, 3, 4, 5] 
## How to Use in Ollama

   1. Update Ollama: Ensure you are running the latest version (v0.6 or higher), as V4 support was added in January/April 2026.
   2. Sign In: Cloud models require an Ollama account. Use ollama signin in your terminal.
   3. Run the Model:
   
   ollama run deepseek-v4-flash:cloud
   
   [2, 6, 7] 

## How to Achieve Better Results (Reasoning Modes)
Unlike the older R1-14B preview, which had fixed reasoning, V4-Flash supports dynamic reasoning effort. To get better results for complex tasks (math, deep logic, or coding), you must call it using specific "thinking" parameters: [2, 8, 9] 

* Toggle Thinking Mode: You can turn reasoning on or off during a session using /set think or /set nothink.
* Max Effort (Recommended for "Reasoning"): For tasks where the 14B model previously struggled, use the Max reasoning effort. In Ollama's CLI, you can force this by adding it to your prompt or setting it in an interactive session:
* High (Default): Good for general chat and simple coding.
   * Max: Required for frontier-level math and complex agentic tasks.
* Prompting Tip: V4-Flash is sensitive to its input structure. For reasoning tasks, ensure you include instructions directly in the user prompt (avoid complex system prompts) and use directives like "Please reason step by step". [1, 8, 9, 10, 11, 12] 
* 

## Integration with Coding Agents
If your goal is better coding performance than the R1-14B, the new model is designed to be "launched" into specific agentic tools rather than just used for chat: [2, 13] 

* Claude Code: ollama launch claude --model deepseek-v4-flash:cloud
* OpenClaw: ollama launch openclaw --model deepseek-v4-flash:cloud [14] 
* 

These tools automatically set the model to max reasoning effort to handle multi-file coding and debugging. [8, 9, 15] 

To call DeepSeek-V4-Flash programmatically via Ollama, you use the standard ollama Python library. The key to getting better results than the old 14B model is leveraging the options dictionary to control the reasoning budget (introduced in Ollama v0.6).
First, install the library if you haven't:

pip install ollama

## Python Example with Reasoning Control

import ollama
def solve_with_reasoning(prompt):
    # Call the cloud-hosted V4-Flash model
    response = ollama.chat(
        model='deepseek-v4-flash:cloud',
        messages=[{'role': 'user', 'content': prompt}],
        options={
            # New V4-specific parameters
            'think': True,           # Enable the "thinking" process
            'think_effort': 'max',   # Options: 'none', 'high', 'max'
            'temperature': 0.6,      # Lower temp helps reasoning stability
            'num_ctx': 32768         # Adjust context window as needed (supports up to 1M)
        }
    )
    
    # The output includes the 'thinking' trace and the final answer
    return response['message']['content']
# Example complex taskprompt = "Write a Rust function to handle concurrent websocket connections with a custom heartbeat mechanism."
print(solve_with_reasoning(prompt))

## Why this beats the 14B version:

   1. think_effort: 'max': This forces the model to use its full 13B active parameter reasoning cycle. The old R1-14B had a "static" reasoning length; V4-Flash can extend its internal chain of thought based on this parameter.
   2. Native MoE Efficiency: Since V4-Flash is a Mixture-of-Experts model, it accesses specialized "coding" or "math" experts that the dense 14B Qwen-based models lacked.
   3. Context Management: By setting num_ctx, you can leverage the model's new 1M token capacity, which allows it to "read" your entire codebase before reasoning—something the 14B preview struggled with due to context compression.

Do you need help setting up the environment variables for the Ollama Cloud authentication?



[1] [https://pub.towardsai.net](https://pub.towardsai.net/i-tested-all-4-deepseek-v4-modes-on-20-real-tasks-the-0-04-flash-won-7-of-them-0ef0fb5c1771)
[2] [https://webscraft.org](https://webscraft.org/blog/deepseek-v4-flash-u-2026-scho-tse-skilki-koshtuye-i-yak-zapustiti-bez-gpu?lang=en)
[3] [https://webscraft.org](https://webscraft.org/blog/deepseek-v4-flash-u-2026-scho-tse-skilki-koshtuye-i-yak-zapustiti-bez-gpu?lang=en)
[4] [https://www.youtube.com](https://www.youtube.com/watch?v=UcSPD64453U#:~:text=DeepSeek%20has%20released%20two%20editions%20of%20V4:,V4%20Flash%20is%20also%20available%20and%20functional.)
[5] [https://framia.pro](https://framia.pro/page/en-US/news/run-deepseek-v4-locally)
[6] [https://www.youtube.com](https://www.youtube.com/watch?v=oHnXPWaFn7k&t=25)
[7] [https://www.reddit.com](https://www.reddit.com/r/AISEOInsider/comments/1swej13/deepseek_v4_ollama_turns_a_simple_terminal_setup/)
[8] [https://api-docs.deepseek.com](https://api-docs.deepseek.com/guides/thinking_mode)
[9] [https://medium.com](https://medium.com/data-science-in-your-pocket/deepseek-v4-pro-vs-deepseek-v4-flash-9e235b74b0d0)
[10] [https://ollama.com](https://ollama.com/library/deepseek-v4-flash#:~:text=3%20Thinking%20modes:%20*%20No%20thinking:%20used,maximum%20reasoning%20effort%20on%20the%20hardest%20problems.)
[11] [https://ollama.com](https://ollama.com/blog/thinking)
[12] [https://www.bentoml.com](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)
[13] [https://ollama.com](https://ollama.com/library/deepseek-v4-flash)
[14] [https://medium.com](https://medium.com/@joe.njenga/i-tried-new-deepseek-v4-on-claude-code-hermes-agent-this-is-wild-bbb769de8d65)
[15] [https://ollama.com](https://ollama.com/library/deepseek-v4-pro)
