# nnTrainFlow
demo of workflows for rapid NN training using remote data center AI systems.

Two applications are included:

**[BraggNN](https://github.com/lzhengchun/nnTrainFlow/tree/main/BraggNN)** based on experimental data, [Recorded Demo](https://youtu.be/cjhv4vepfv0) and 

**[CookieNetAE](https://github.com/lzhengchun/nnTrainFlow/tree/main/CookieNetAE)** using data generated from simulation, [Recorded Demo](https://youtu.be/4hi9AoGUJ78). 

**Note that**:
These two flows run in production across restricted machines.
As the endpoint, flow and funcX functions used in this repo are private to author's account, one should not expect to run the flows directly from another account. Instead, reader can use these demo flows as template to recreate the flow for other application scenarios.

![The Big Picture](BigPic.png)

Details of the Model and Data service (currently not yet integrated in this flow implementation) on the right-hand side of the big picture can be found from this paper:
[fairDMS: Rapid Model Training by Data and Model Reuse](https://arxiv.org/abs/2204.09805)

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

@inproceedings{fairdms,  
  author = {Ali, Ahsan and Sharma, Hemant and Kettimuthu, Rajkumar and Kenesei, Peter and Trujillo, Dennis and Miceli, Antonino and Foster, Ian and Coffee, Ryan and Thayer, Jana and Liu, Zhengchun},
  keywords = {Machine Learning, Representation Learning, FAIR},
  title = {fairDMS: Rapid Model Training by Data and Model Reuse},
  booktitle = {2022 IEEE International Conference on Cluster Computing (CLUSTER)},
  publisher = {IEEE},
  year = {2022},
}

```
