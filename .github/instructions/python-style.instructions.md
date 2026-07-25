---
applyTo: "**/*.py"
---

# Write the code as if you are handing it to John

John is a teammate who is brand new to Python. Every rule below exists so John can read the
code without asking anyone a question.

1. **Keep each function short.** If John cannot read it on one screen, split it.
2. **Use clear names.** `create_payment` is good. `cp` is not.
3. **Say what kind of value you expect.** If an amount is a number, write it so John can see
   at a glance that it is a number.
4. **One job per function.** A function either checks a rule, or saves data — not both.
5. **Comment only the business reason, never the obvious.** Good: `# reject amounts over 250000 (bank rule BR-1)`. Bad: `# add one to x`.
6. **The code should already answer "what does this do?"** before John has to ask.
