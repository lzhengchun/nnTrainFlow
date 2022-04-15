This is a workflow, based on Globus Flow service, to rapidally train [CookieNetAE](https://github.com/AISDC/CookieNetAE) using remote AI systems such as GPU clusters, SambaNova, Cerebras, GraphCore etc.

Steps in the flow including:

1. [CookieSimSlim](https://github.com/ryancoffee/CookieSimSlim) simulator to generate data, (funcX)
2. post-process data as training/validation datasets (funcX)
3. transfer them to an AI system (globus transfer)
4. Training CookieNetAE model (funcX)
5. Transfer trained model and traces to SLAC (Globus transfer)
