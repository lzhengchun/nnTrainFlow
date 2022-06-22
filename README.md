# nnTrainFlow
demo of workflows for rapid NN training using remote data center AI systems.

Two applications are included:

**[BraggNN](https://github.com/lzhengchun/nnTrainFlow/tree/main/BraggNN)** based on experimental data and 

**[CookieNetAE](https://github.com/lzhengchun/nnTrainFlow/tree/main/CookieNetAE)** using data generated from simulation. 

**Note that**:
These two flows run in production across restricted machines.
As the endpoint, flow and funcX functions used in this repo are private to author's account, one should not expect to run the flows directly from another account. Instead, reader can use these demo flows as template to recreate the flow for other application scenarios.

![The Big Picture](BigPic.png)


## Citation
If you use this code for your research, please cite our paper:

- Zhengchun Liu, Ahsan Ali, Peter Kenesei, Antonino Miceli, Hemant Sharma, Nicholas Schwarz, Dennis Trujillo et al. "Bridging Data Center AI Systems with Edge Computing for Actionable Information Retrieval." In 2021 3rd Annual Workshop on Extreme-scale Experiment-in-the-Loop Computing (XLOOP), pp. 15-23. IEEE, 2021.

Or via bibtex

```
@inproceedings{liu2021bridging,
  title={Bridging Data Center AI Systems with Edge Computing for Actionable Information Retrieval},
  author={Liu, Zhengchun and Ali, Ahsan and Kenesei, Peter and Miceli, Antonino and Sharma, Hemant and Schwarz, Nicholas and Trujillo, Dennis and Yoo, Hyunseung and Coffee, Ryan and Layad, Naoufal and others},
  booktitle={2021 3rd Annual Workshop on Extreme-scale Experiment-in-the-Loop Computing (XLOOP)},
  pages={15--23},
  year={2021},
  organization={IEEE}
}

```
