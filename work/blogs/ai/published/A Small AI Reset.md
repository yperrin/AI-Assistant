# A Small AI Reset

**By:** [Yann Perrin](https://clarivate.atlassian.net/wiki/spaces/LSHT/blog/2026/03/08/192512441/A+Small+AI+Reset)  
**Date:** March 08, 2026  
**Read Time:** 3 min

I was not sure everyone was reading those, so every week I wonder whether I should stop. I am told they are indeed read and so if you want to make sure I keep those up, please make sure to give it a thumbs up.

Also, in sync with my trip to India and me presenting a state of the Union for AI in SDLC, I plan on giving a quick reset on what we have and some somewhat random predictions. This is meant to only describe using AI for producing software and not really for including AI in content and product software offerings.

---

## Technics

### Prompt Engineering
First, you need to know how to talk to AI, this is the basic skill and the starting point. The same prompt will not work with different models. Even though an argument can be made that with the models are getting so good, we can speak directly to the models and it will figure out what we need. But it is not that simple, you still need to know how to talk AI to be efficient. There are different classes available, I bought the google a life time ago now. Look for a class teaching principles and hopefully not something specific to a model.

### Context Engineering
This is the next step. The models are so good those days, which high-end model we use is not as important as the information we feed it. The process and how we pass the data is more important than which model you selected (got high-end ones). Visual Studio code now provide tools to visualize context usage.

If you have too many tools, too many attachments, too long of a history the models will not be able to work well. There are ways you can also compact the context but some information will be lost.

Gemini 3 was until recently the best model at handling large contexts and so it made sense to use those models to go through the code base to create a plan. Then you can use a different model to actually implement the plan. The plan should contain only the context needed to implement the current requirement and no longer the full context needed to do the necessary research. Mastering context also means mastering skills, custom agents, sub-agents, etc. So it is by no means a small task.

### Memory
This is a little more advanced, but once you can reliably run your agents, Anthropic in particular, companies made a lot of progress on how long you can run an agent continuously. This brings us also to a mode where you want an agent to learn how you work, what you need to ensure it gets better over time. This requires a system to store a memory the agent can refer to and that it uses as part of all its operation to be more and more personalized to what you need it to do.

Also kind of refer to the shared memory multiple agents would need in order to coordinate their work and findings.

---

## Wild Ass Guesses about where we are going

Those are guesses because it is changing so fast, it is very difficult to have a good read.

### The job is not going away but it will change
We need people who understand the domain, understand what we should be working on. We now need to orchestrate the work AI does. We need to focus on intent and become experts at passing the intent (as well as requirements) to the agent so it can make intelligent decisions.

The more we are able to create software, the easier it is, the more we will create and the more people we will need to implement all this.

### Multi-independent agents running for a long time
It is already happening, we will be able to throw agents a long problem, they will work on it for a day or 2 and then create something that would have taken months for a team of people to do. It can be look at the market, compare the competition and tell me what segments and new opportunities I should be focusing on. Or it could be create a new Operating System for me to host agent generated code. Or probably find new proteins, chemical compounds targetting those proteins, etc.

### AI comes to where you need it
You no longer need to go to a web site and chat with an agent. AI is running in your glasses, recoding all your conversations from a pin on your jacket, running the small robot in your body checking you blood and injecting medicine directly before you know you needed it. Some of those scenarios of course are already there but the trend is pretty clear. Give me my data and intelligence to act on my data where I need it, when I need it. It could be a text message indicating my flight has been changed and a new hotel reservation was made automatically.

### Understanding 3D world is close
There are quite a few models and companies now working on understanding the world and how to interact with the physical objects of this world. This can be used to create games, movies, etc. It could also help AI give you an alert in your glasses to let you know if you don’t move you will have an accident in the physical world.

### Robots are the new frontier
AI models are smaller and smaller; they can be embedded in smaller physical objects. Combine this with an understanding of the 3d and physical world and now they can pick up the shirt on the floor, put it in the laundry, wash it, fold it and of course so much more.

---

## What can you do
First, AI is everywhere; it is already a requirement for job applicants, so no work should be accomplished today without the help of AI.

**Be Curious** is the short version. This is a strange skill. You cannot learn this like you learn a new language; it requires a change in how you think. It needs to be practiced.

Start learning, start using in every day task. Have conversations with AI to exponentially learn. The more who do it, the better at it you are and the easier it is to learn more.