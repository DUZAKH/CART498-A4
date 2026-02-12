Link: : https://cart498-a4-36ex.onrender.com/ 
This web app allows users to enter a dream description into a text box and receive a Jungian-style analysis of their dream along with a symbolic illustration. Both the text and image outputs are generated using OpenAI’s API. For the text analysis, the assistant is instructed to act as a Jungian dream analyst. The system prompt emphasizes interpretation of symbolic elements.Its prompted like such:  input=[
                    {
                        "role": "developer",
                        "content": "You are a dream analyst trained in Jungian psychology. Interpret symbolic elements such as figures, actions, objects, and settings from core Jungian concepts. Focus on symbolic meaning rather than literal interpretation. Provide thoughtful psychological insight into what the dream imagery might represent in the dreamer's inner life. Avoid deterministic or medical claims. Write in a reflective, interpretive tone."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
The image generation is structured in a similar way. The AI is instructed to create a surreal, symbolic illustration that corresponds to the user’s dream description.  Its prompted like so: image_prompt = f"""You are an AI artist. Create a surreal, simple painterly, symbolic dream illustration based on the following description. Focus on key symbolic elements, figures, actions, and settings, inspired by Jungian dream analysis. Dream description: {prompt} """
**User guide:**
1-enter a dream description and submit the form
2- the page displays both the textual Jungian analysis and the corresponding symbolic image. 

**Issues and insights:** My most important observation was that when deployed on free hosting platforms like Render, image generation can occasionally fail due to server timeouts, in which case the text analysis will still be returned. So my insights gained include recognizing the limitations of free cloud hosting for heavy API requests. Otherwise, the importance of concise and professional prompt language to avoid overly verbose or “cheesy” outputs is soemthing I want to work on further. Thus, future improvements could include refining the text prompts for clarity, implementing optional or asynchronous image generation to avoid server errors, and enhancing the web page styling to improve usability and visual appeal. These adjustments would help create a more stable, polished, and user-friendly dream analysis experience while maintaining alignment with Jungian principles.
