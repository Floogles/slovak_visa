# slovak_visa
NOT TO BE WIDELY USED, MADE AS A FAVOUR TO OTHERS.

Made to help a relative book a visa at the Slovakian embassy on their online systems. Only works on the Slovakian website and personal info has been redacted.

Every few minutues the code logs into an account, chooses the embassy locations to search (in this case Moscow and St. Petersburg) and searches for available visa appointments. If an empty slot is found, it sends a Telegram to the designated recipient to make them aware at which embassy a slot is open and instructs them to log in and book ASAP.

Fairly basic code, and if implemented again I would use RegEx and stop using Schedule to make the code more efficient and more generally applicable.
