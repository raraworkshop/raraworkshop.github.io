---
layout: project
urltitle:  "Natural Language Reasoning and Structured Explanations Workshop"
title: "Natural Language Reasoning and Structured Explanations Workshop"
categories: workshop, computer vision, natural language, grounding, interaction, machine learning, vigil, naacl, 2021
permalink: /
bibtex: true
paper: true
acknowledgements: ""
---

<!-- <br /> -->
<!-- <div class="row" id="title">
  <div class="col-xs-12">
    <center><h1>Natural Language Reasoning and Structured Explanations Workshop</h1></center>
    <center><h2>July 13-14, 2023 @ ACL 2023. Toronto, Canada.</h2></center>
 
    
    
  </div>
</div> -->

<br />

<div class="row">
    <div class="col-xs-12">
    <p><b>Note: the deadline has been extended until May 3. See below for important dates.</b>
        <p>
          With recent scaling of large pre-trained Transformer language models (LLMs), the scope of feasible NLP tasks has broadened. Significant recent work has focused on tasks that require some kind of natural language reasoning. A trajectory in question answering has led us from extraction-oriented datasets like SQuAD to “multi-hop” reasoning datasets like HotpotQA and StrategyQA. Although LLMs have shown remarkable performance on most NLP tasks, it is often unclear why their answers follow from what they know. To address this gap, a new class of explanation techniques has emerged which play an integral part in structuring the reasoning necessary to solve these datasets. For example, the chain-of-thought paradigm leverages explanations as vehicles for LLMs to mimic human reasoning processes. Entailment trees offer a way to ground multi-step reasoning in a collection of verifiable steps. Frameworks like SayCan bridge high-level planning in language and with low-level action trajectories. As a result, we see a confluence of methods blending explainable machine learning/NLP, classical AI (especially theorem proving), and cognitive science (how do humans structure explanations?). This workshop aims to bring together a diverse set of perspectives from these different traditions and attempt to establish common ground for how these various kinds of explanation structures can tackle a broad class of reasoning problems in natural language and beyond.
        </p>
<br />

<!-- Schedule -->
<div class="row" id="schedule">
  <div class="col-md-4 col-xs-12">
    <h2>Schedule</h2>
  </div>
  <div class="col-md-8 col-xs-12">
      <select id="timezone-select" class="form-control"></select>
  </div>
</div>
<div class="row">
  <div class="col-xs-12">
    <table class="table table-striped" id="schedule-table">
    <tbody>
    <tr> <th scope="row" data-time="08:00">08:00 AM</th> <td>Virtual Poster Session 1</td></tr>
    <tr> <th scope="row" data-time="09:00">09:00 AM</th> <td>Opening Remarks</td></tr>
    <tr> <th scope="row" data-time="09:10">09:10 AM</th> <td>
      Invited Speaker: Ellie Pavlick<br />
      <span style="font-style:italic">Mechanistic Evidence of Structured Reasoning in LLMs</span>
      <!-- <a data-toggle="collapse" href="#schedule-talk1" aria-cexpanded="false" aria-controls="schedule-talk1">[Abstract]</a>
      <div class="collapse" id="schedule-talk1">
        Abstract: Computational systems for grounded language understanding have seen impressive advances over the last decade, due largely to advances in multimodal datasets, neural and symbolic modeling techniques, and computational power. But human meaning interpretation in grounded contexts remains far deeper and more sophisticated. In this talk I describe several recent studies in our research group that illustrate the subtlety and richness of human meaning interpretation using very simple, experimentally controlled utterances and visual grounding contexts. These studies shed light on the compositional structure of the semantic representations underlying human language comprehension, their relationship with the pragmatic inference mechanisms that support contextually conditioned interpretation, and the likely requirements for truly human-like language understanding in artificial systems.
      </div> -->
    </td></tr>
    <tr> <th scope="row" data-time="09:50">09:50 AM</th> <td>
      Invited Speaker: Noah Goodman<br />
      <span style="font-style:italic">[Talk title forthcoming]</span>
      <!-- <a data-toggle="collapse" href="#schedule-talk2" aria-cexpanded="false" aria-controls="schedule-talk2">[Abstract]</a>
      <div class="collapse" id="schedule-talk2">
        Abstract: Robots can act as a force multiplier for people, whether a robot assisting an astronaut with a repair on the International Space station, a UAV taking flight over our cities, or an autonomous vehicle driving through our streets. Existing approaches use action-based representations that do not capture the goal-based meaning of a language expression and do not generalize to partially observed environments.  The aim of my research program is to create autonomous robots that can understand complex goal-based commands and execute those commands in partially observed, dynamic environments.  I will describe demonstrations of object-search in a POMDP setting with information about object locations provided by language, and mapping between English and Linear Temporal Logic, enabling a robot to understand complex natural language commands in city-scale environments.  These advances represent steps towards robots that interpret complex natural language commands in partially observed environments using a decision theoretic framework.
      </div> -->
    </td></tr>
    <tr> <th scope="row" data-time="10:30">10:30 AM</th> <td>Break 1</td></tr>
    <tr> <th scope="row" data-time="11:00">11:00 AM</th> <td>
      Oral Presentation: Li Zhang, Liam Dugan, Hainiu Xu and Chris Callison-burch<br />
      <span style="font-style:italic">Exploring the Curious Case of Code Prompts</span>
      <a data-toggle="collapse" href="#schedule-talk3" aria-cexpanded="false" aria-controls="schedule-talk3">[Abstract]</a>
      <div class="collapse" id="schedule-talk3">
        Abstract: Recent work has shown that prompting language models with code-like representations of natural language leads to performance improvements on structured reasoning tasks. However, such tasks comprise only a small subset of all natural language tasks. In our work, we seek to answer whether or not code-prompting is the preferred way of interacting with language models in general. We compare code and text prompts across three popular GPT models (davinci, code-davinci-002, and text-davinci-002) on a broader selection of tasks (e.g., QA, sentiment, summarization) and find that with few exceptions, code prompts do not consistently outperform text prompts. Furthermore, we show that the style of code prompt has a large effect on performance for some (but not all) tasks and that fine-tuning on text instructions leads to better relative performance of code prompts.
      </div>
    </td> </tr>
    <tr> <th scope="row" data-time="11:10">11:10 AM</th> <td>
      Oral Presentation: Vanya Cohen and Raymond Mooney<br />
      <span style="font-style:italic">Using Planning to Improve Semantic Parsing of Instructional Texts</span>
      <a data-toggle="collapse" href="#schedule-talk4" aria-cexpanded="false" aria-controls="schedule-talk4">[Abstract]</a>
      <div class="collapse" id="schedule-talk4">
        Abstract: We develop a symbolic planning-based decoder to improve the few-shot semantic parsing of instructional texts. The system takes long-form instructional texts as input and produces sequences of actions in a formal language that enable execution of the instructions. This task poses unique challenges since input texts may contain long context dependencies and ambiguous and domain-specific language. Valid semantic parses also require sequences of steps that constitute an executable plan. We build on recent progress in semantic parsing by leveraging large language models to learn parsers from small amounts of training data. During decoding, our method employs planning methods and domain information to rank and correct candidate parses. To validate our method, we evaluate on four domains: two household instruction-following domains and two cooking recipe interpretation domains. We present results for few-shot semantic parsing using leave-one-out cross-validation. We show that utilizing planning domain information improves the quality of generated plans. Through ablations we also explore the effects of our decoder design choices.
      </div>
    </td></tr>
    <tr> <th scope="row" data-time="11:20">11:20 PM</th> <td>In-Person Poster Session 1 / Virtual Poster Session 2 (See posters below)</td></tr>
    <tr> <th scope="row" data-time="12:20">12:20 PM</th> <td>Lunch</td> </tr>
    <tr> <th scope="row" data-time="13:30">13:30 PM</th> <td>In-Person Poster Session 2 (See posters below)</td> </tr>
    <tr> <th scope="row" data-time="14:30">14:30 PM</th> <td>
      Oral Presentation: Jinheon Baek, Alham Fikri Aji and Amir Saffari<br />
      <span style="font-style:italic">Knowledge-Augmented Language Model Prompting for Zero-Shot Knowledge Graph Question Answering</span>
      <a data-toggle="collapse" href="#schedule-talk5" aria-cexpanded="false" aria-controls="schedule-talk5">[Abstract]</a>
      <div class="collapse" id="schedule-talk5">
        Abstract: Large Language Models (LLMs) are capable of performing zero-shot closed-book question answering tasks, based on their internal knowledge stored in parameters during pre-training. However, such internalized knowledge might be insufficient and incorrect, which could lead LLMs to generate factually wrong answers. Furthermore, fine-tuning LLMs to update their knowledge is expensive. To this end, we propose to augment the knowledge directly in the input of LLMs. Specifically, we first retrieve the relevant facts to the input question from the knowledge graph based on semantic similarities between the question and its associated facts. After that, we prepend the retrieved facts to the input question in the form of the prompt, which is then forwarded to LLMs to generate the answer. Our framework, Knowledge-Augmented language model PromptING (KAPING), requires no model training, thus completely zero-shot. We validate the performance of our KAPING framework on the knowledge graph question answering task, that aims to answer the user's question based on facts over a knowledge graph, on which ours outperforms relevant zero-shot baselines by up to 48% in average, across multiple LLMs of various sizes.
      </div>
    </td> </tr>
    <tr> <th scope="row" data-time="14:40">14:40 PM</th> <td>
      Oral Presentation: Michal Štefánik and Marek Kadlcik<br />
      <span style="font-style:italic">Can In-context Learners Learn a Reasoning Concept from Demonstrations?</span>
      <a data-toggle="collapse" href="#schedule-6" aria-cexpanded="false" aria-controls="schedule-6">[Abstract]</a>
      <div class="collapse" id="schedule-6">
        Abstract: Large language models show an emergent ability to learn a new task from a small number of input-output demonstrations. However, recent work shows that in-context learners largely rely on their pre-trained knowledge, such as the sentiment of the labels, instead of finding new associations in the input. However, the commonly-used few-shot evaluation settings using a random selection of in-context demonstrations can not disentangle models' ability to learn a new skill from demonstrations, as most of the randomly-selected demonstrations do not present relations informative for prediction beyond exposing the new task distribution.
        To disentangle models' in-context learning ability independent of models' memory, we introduce a Conceptual few-shot learning method selecting the demonstrations sharing a possibly-informative concept with the predicted sample. We extract a set of such concepts from annotated explanations and measure how much can models benefit from presenting these concepts in few-shot demonstrations.
        We find that smaller models are more sensitive to the presented concepts. While some of the models are able to benefit from concept-presenting demonstrations for each assessed concept, we find that none of the assessed in-context learners can benefit from all presented reasoning concepts consistently, leaving the in-context concept learning an open challenge.
      </div>
    </td> </tr>
    <tr> <th scope="row" data-time="14:50">14:50 PM</th> <td>
      Invited Speaker: Peter Clark<br />
      <span style="font-style:italic">The role of NL reasoning in the age of GPT</span>
      <a data-toggle="collapse" href="#schedule-talk7" aria-cexpanded="false" aria-controls="schedule-talk7">[Abstract]</a>
      <a data-toggle="collapse" href="#speaker-bio-talk7" aria-cexpanded="false" aria-controls="speaker-bio-talk7">[Speaker Bio]</a>
      <div class="collapse" id="schedule-talk7">
        Abstract: While the performance of new LLMs is stunning, it remains unclear how (or even if) an answer follows from their latent "beliefs" about the world, or whether an LLM even has a coherent internal belief system. In this talk I'll describe recent work we have done to probe a model's beliefs, construct interpretable representations of how the model's answers systematically follow from them, and how a broader system can identify and repair inconsistencies that may exist among those beliefs. More generally, I'll promote architectures in which interpretable, systematic NL reasoning and LLM-style reasoning co-exist in a broader system, allowing both styles of reasoning to inform each other, and paving the way for more interactive systems where users can probe, argue with, learn from, and teach our future companions.
      </div>
      <div class="collapse" id="speaker-bio-talk7">
        Peter Clark is a Senior Director and the interim CEO at the Allen Institute for AI (AI2), and leads the Aristo Project. His work focuses on natural language processing, machine reasoning, and world knowledge, and the interplay between these three areas.
      </div>
    </td> </tr>
    <tr> <th scope="row" data-time="15:30">15:30 PM</th> <td>Break 2</td></tr>
    <tr> <th scope="row" data-time="16:00">16:00 PM</th> <td>
      Invited Speaker: Denny Zhou<br />
      <span style="font-style:italic">Teach Language Models to Reason</span>
      <a data-toggle="collapse" href="#schedule-talk8" aria-cexpanded="false" aria-controls="schedule-talk8">[Abstract]</a>
      <a data-toggle="collapse" href="#speaker-bio-talk8" aria-cexpanded="false" aria-controls="speaker-bio-talk8">[Speaker Bio]</a>
      <div class="collapse" id="schedule-talk8">
        Over the past decades, the machine learning community has developed a multitude of data-driven techniques aimed at enhancing learning efficiency. These include semi-supervised learning, meta learning, active learning, transfer learning, and more. However, none of these techniques have proven to be highly effective for real-world natural language processing tasks. This shortcoming uncovers a fundamental flaw in machine learning - the absence of reasoning. Humans often learn from just a few examples because of their capacity to reason, as opposed to relying on data statistics. In this talk, I will talk about the large language models (LLM)  reasoning work that we pioneered, and show that the techniques we developed can greatly narrow the gap between human intelligence and machine learning: crushed SoTA in the literature while demanding only a few annotated examples and no training. Our work was showcased at Google I/O 2022 by Google CEO Sundar Pichai.
      </div>
      <div class="collapse" id="speaker-bio-talk8">
        Denny Zhou is a principal scientist / research director in Google DeepMind, where he is the founder and current lead of the Reasoning Team. His primary research interest is building and teaching large language models (LLMs) with an ambitious goal of attaining human-level reasoning capabilities within these models. His team in Google has developed chain-of-thought prompting, self-consistency decoding, least-to-most prompting, instruction tuning (FLAN2), LLMs self-debugging and various investigations of emergent properties of LLMs. He won Google Research Tech Impact Award in 2022.
      </div>
    </td> </tr>
    <tr> <th scope="row" data-time="16:40">16:40 PM</th> <td>
      Invited Speaker: Sarah Wiegraffe
       <span style="font-style:italic">Two Views of Language Model Interpretability</span>
      <a data-toggle="collapse" href="#schedule-talk9" aria-cexpanded="false" aria-controls="schedule-talk9">[Abstract]</a>
      <a data-toggle="collapse" href="#speaker-bio-talk9" aria-cexpanded="false" aria-controls="speaker-bio-talk9">[Speaker Bio]</a>
      <div class="collapse" id="schedule-talk9">
        When generating text from language models (LMs), many prompting methods strive to explain LM behavior by eliciting specifically-structured outputs (e.g, chain-of-thought prompting). Relatedly, querying a model with specially-designed inputs and observing output behavior is a longstanding and popular method in the NLP interpreter’s toolbox. Prompting and querying approaches explain how LMs operate at a high-level (in natural language) without attributing behaviors to any specific components of the network. A separate line of work has investigated attributing or attempting to reconstruct model behaviors at the model parameter or hidden representation-level, generally at a small scale. While these two techniques often seem at odds in terms of their stated aims, they collectively inform a large progression in our understanding of LMs in the past 2 years. In this talk, I will give examples of both of these approaches, highlight their similarities and differences, and discuss paths forward that leverage their combined strengths.
      </div>
      <div class="collapse" id="speaker-bio-talk9">
         Sarah Wiegreffe is a Young Investigator (postdoc) at the Allen Institute of AI, where she is a member of the Aristo team. She also holds a courtesy appointment in the Allen School at the University of Washington. Her research interests encompass interpretability + explainability of NLP models, with a focus on the faithfulness of generated text to internal LM prediction mechanisms and the utility of model-generated textual explanations to humans. She received her PhD in 2022 from Georgia Tech, advised by Mark Riedl. She also received an M.S. in Computer Science (2020) and B.S. in Data Science (2017) from Georgia Tech and the College of Charleston, respectively. Outside of work, she enjoys rock climbing, cooking, and exploring Seattle.
      </div>
    </td> </tr>
    </tbody>
    </table>
  </div>
</div>


<hr />

<!-- Speakers -->
<div class="row" id="speakers">
  <div class="col-xs-12">
    <h2>Speakers</h2>
  </div>
</div>
<div class="row">
  <div class="col-xs-6 col-lg-3">
    <a href="https://allenai.org/team/peterc">
      <img class="people-pic" src="https://images.ctfassets.net/wf5t1ptx352c/30A5DGuNxSgIm2Kso0OIcg/0308a951718f1b8061e354a12b0c5ec5/Peter-Clark.jpg?w=320&h=320&fit=fill">
    </a>
    <div class="people-name">
      <a href="https://allenai.org/team/peterc">Peter Clark</a>
      <h6>Allen Institute for AI</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://cs.brown.edu/people/epavlick/">
      <img class="people-pic" src="http://cs.brown.edu/people/epavlick/profile-pic-circle.gif">
    </a>
    <div class="people-name">
      <a href="https://cs.brown.edu/people/epavlick/">Ellie Pavlick</a>
      <h6>Brown University</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://dennyzhou.github.io/">
      <img class="people-pic" src="https://dennyzhou.github.io/unnamed.jpeg">
    </a>
    <div class="people-name">
      <a href="https://dennyzhou.github.io/">Denny Zhou</a>
      <h6>Google AI</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://cocolab.stanford.edu/ndg">
      <img class="people-pic" src="https://cocolab.stanford.edu/images/members/noah.jpg">
    </a>
    <div class="people-name">
      <a href="https://cocolab.stanford.edu/ndg">Noah Goodman</a>
      <h6>Stanford University</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://sarahwie.github.io/">
      <img class="people-pic" src="{{ "/static/img/people/sarah_wiegraffe.jpg" | prepend:site.baseurl }}">
    </a>
    <div class="people-name">
      <a href="https://sarahwie.github.io/">Sarah Wiegreffe</a>
      <h6>Allen Institute for AI</h6>
    </div>
  </div>
</div>

<hr />

<div class="row" id="accepted">
  <div class="col-xs-12">
    <h2>Accepted Papers</h2>
    <p>Note: 2 additional papers were accepted but are not listed here because of an anonymity period.</p>
  </div>
</div>

<h3>Virtual Poster Session 1</h3>
<ul class="paper-list">
<li>
<span class="paper-title">Case-Based Reasoning with Language Models for Classification of Logical Fallacies</span><br>
<span class="paper-authors">Zhivar Sourati, Filip Ilievski, Hông-Ân Sandlin and Alain Mermoud</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Choice-75: A Dataset on Decision Branching in Script Learning</span><br>
<span class="paper-authors">Zhaoyi Hou, Li Zhang and Chris Callison-Burch</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Distinguish Before Answer: Generating Contrastive Explanation as Knowledge for Commonsense Question Answering</span><br>
<span class="paper-authors">Qianglong Chen, Guohai Xu, Mingshi Yan, J. Zhang, Fei Huang, Luo Si, Yin Zhang</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">IDOL: Indicator-oriented Logic Pre-training for Logical Reasoning</span><br>
<span class="paper-authors">Zihang Xu, Ziqing Yang, Yiming Cui, Shijin Wang</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Investigating Transformer-Guided Chaining for Interpretable Natural Logic Reasoning</span><br>
<span class="paper-authors">Kanagasabai Rajaraman, Saravanan Rajamanickam, Wei Shi</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">QAMPARI: A Benchmark for Open-domain Questions with Many Answers</span><br>
<span class="paper-authors">Samuel Amouyal, Tomer Wolfson, Ohad Rubin, Ori Yoran, Jonathan Herzig and Jonathan Berant </span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">SConE: Simplified Cone Embeddings with Symbolic Operators for Complex Logical Queries</span><br>
<span class="paper-authors">Chau Nguyen, Tim French, Wei Liu, Michael Stewart</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Segment-Level and Category-Oriented Network for Knowledge-Based Referring Expression Comprehension</span><br>
<span class="paper-authors">Yuqi Bu, Xin Wu, Liuwu Li, Yi Cai, Qingbao Huang, Qiong Liu</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Shall We Pretrain Autoregressive Language Models with Retrieval? A Comprehensive Study</span><br>
<span class="paper-authors">Boxin Wang, Wei Ping, Peng Xu, Lawrence McAfee, Zihan Liu, Mohammad Shoeybi, Yi Dong, Oleksii Kuchaiev, Bo Li, Chaowei Xiao, Anima Anandkumar and Bryan Catanzaro </span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Neural-symbolic Contrastive Learning for Cross-domain Inference</span><br>
<span class="paper-authors">Mingyue Liu, Jialin Yu, Hao Cui, Sara Uckelman and Yang Long </span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>
</ul>

<h3>Virtual Poster Session 2</h3>
<ul class="paper-list">
<li>
<span class="paper-title">Grounded physical language understanding with probabilistic programs and simulated worlds</span><br>
<span class="paper-authors">Cedegao Zhang, Lionel Wong, Gabriel Grand and Josh Tenenbaum</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Hierarchical Prompting Assists Large Language Model on Web Navigation</span><br>
<span class="paper-authors">Chi-Fan Lo, Abishek Sridhar, Hao Zhu, Frank F. Xu and Shuyan Zhou </span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Interpretable Multimodal Misinformation Detection with Logic Reasoning</span><br>
<span class="paper-authors">Hui Liu, Wenya Wang, Haoliang Li</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Logical Reasoning over Natural Language as Knowledge Representation: A Survey</span><br>
<span class="paper-authors">Zonglin Yang, Xinya Du, Rui Mao, Jinjie Ni and Erik Cambria</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">OPT-R: Exploring the Role of Explanations in Finetuning and Prompting for Reasoning Skills of Large Language Models</span><br>
<span class="paper-authors">Badr AlKhamissi, Siddharth Verma, Ping Yu, Zhijing Jin, Asli Celikyilmaz and Mona Diab </span><br>
<span class="paper-type"><span>[Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Synthetic Dataset for Evaluating Complex Compositional Knowledge for Natural Language Inference</span><br>
<span class="paper-authors">Sushma Anand Akoju, Robert Vacareanu, Eduardo Blanco, Haris Riaz and Mihai Surdeanu </span><br>
<span class="paper-type"><span>[Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Tab-CoT: Zero-shot Tabular Chain of Thought</span><br>
<span class="paper-authors">Jin Ziqi, Wei Lu</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Teaching Large Language Models to Self-Debug</span><br>
<span class="paper-authors">Xinyun Chen, Maxwell Lin, Nathanael Schaerli and Denny Zhou </span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

</ul>

<h3>In-Person Poster Session 1</h3>
<ul class="paper-list">
<li>
<span class="paper-title">A smashed glass cannot be full: Generation of Commonsense Explanations through Prompt-based Few-shot Learning</span><br>
<span class="paper-authors">Andrea Zaninello and Bernardo Magnini</span><br>
<span class="paper-type"><span>[Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Answering Questions by Meta-Reasoning over Multiple Chains of Thought</span><br>
<span class="paper-authors">Ori Yoran, Tomer Wolfson, Ben Bogin, Uri Katz, Daniel Deutch and Jonathan Berant </span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Causal Reasoning of Entities and Events in Procedural Texts</span><br>
<span class="paper-authors">Li Zhang, Hainiu Xu, Yue Yang, Shuyan Zhou, Weiqiu You, Manni Arora and Chris Callison-Burch</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">DREAM: Improving Situational QA by First Elaborating the Situation</span><br>
<span class="paper-authors">Yuling Gu, Bhavana Dalvi Mishra and Peter Clark</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Designing harder benchmarks for evaluating zero-shot generalizability in Question Answering over Knowledge Bases</span><br>
<span class="paper-authors">Ritam Dutt, Sopan Khosla, Vinayshekhar Bannihatti Kumar and Rashmi Gangadharaiah </span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes</span><br>
<span class="paper-authors">Cheng-Yu Hsieh, Chun-Liang Li, Chih-Kuan Yeh, Hootan Nakhost, Yasuhisa Fujii, Alexander Ratner, Ranjay Krishna, Chen-Yu Lee, Tomas Pfister</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Effect Graph: Effect Relation Extraction for Explanation Generation</span><br>
<span class="paper-authors">Jonathan Kobbe, Ioana Hulpuș and Heiner Stuckenschmidt </span><br>
<span class="paper-type"><span>[Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Evaluating statistical language models as pragmatic reasoners</span><br>
<span class="paper-authors">Benjamin Lipkin, Lionel Wong, Gabriel Grand and Josh Tenenbaum</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Examining the Emergence of Deductive Reasoning in Generative Language Models</span><br>
<span class="paper-authors">Peter Belcak, Luca Lanzendörfer and Roger Wattenhofer</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Explanation Regeneration via Information Bottleneck</span><br>
<span class="paper-authors">Qintong Li, Zhiyong Wu, Lingpeng Kong, Wei Bi</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Hypothetical Training for Robust Machine Reading Comprehension of Tabular Context</span><br>
<span class="paper-authors">Moxin Li, Wenjie Wang, Fuli Feng, Hanwang Zhang, Qifan Wang, Tat-Seng Chua</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">I Spy a Metaphor: Large Language Models and Diffusion Models Co-Create Visual Metaphors</span><br>
<span class="paper-authors">Tuhin Chakrabarty, Arkadiy Saakyan, Olivia Winn, Artemis Panagopoulou, Yue Yang, Marianna Apidianaki, Smaranda Muresan</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Interpretable Math Word Problem Solution Generation Via Step-by-step Planning</span><br>
<span class="paper-authors">Mengxue Zhang, Zichao Wang, Zhichao Yang, Weiqi Feng and Andrew Lan</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Knowledge-Augmented Language Model Prompting for Zero-Shot Knowledge Graph Question Answering</span><br>
<span class="paper-authors">Jinheon Baek, Alham Fikri Aji and Amir Saffari </span><br>
<span class="paper-type"><span style="color:#DD3333;font-weight:700">[Oral, Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Learning to Perform Complex Tasks through Compositional Fine-Tuning of Language Models</span><br>
<span class="paper-authors">Victor Bursztyn, David Demeter, Doug Downey and Larry Birnbaum</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">PINTO: Faithful Language Reasoning Using Prompt-Generated Rationales</span><br>
<span class="paper-authors">Peifeng Wang, Aaron Chan, Filip Ilievski, Muhao Chen and Xiang Ren</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Reasoning Circuits: Few-shot Multi-hop Question Generation with Structured Rationales</span><br>
<span class="paper-authors">Saurabh Kulshreshtha and Anna Rumshisky</span><br>
<span class="paper-type"><span>[Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Reasoning in Large Language Models Through Symbolic Math Word Problems</span><br>
<span class="paper-authors">Vedant Gaur, Nikunj Saunshi</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Reasoning with Language Model Prompting: A Survey</span><br>
<span class="paper-authors">Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang and Huajun Chen</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Recursion of Thought: A Divide-and-Conquer Approach to Multi-Context Reasoning with Language Models</span><br>
<span class="paper-authors">Soochan Lee, Gunhee Kim</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Reimagining Retrieval Augmented Language Models for Answering  Queries</span><br>
<span class="paper-authors">Wang-Chiew Tan, Yuliang Li, Pedro Rodriguez, Richard James, Xi Victoria Lin, Alon Halevy, Wen-tau Yih</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">STREET: A Multi-Task Structured Reasoning and Explanation Benchmark</span><br>
<span class="paper-authors">Danilo Neves Ribeiro, Shen Wang, Xiaofei Ma, Henghui Zhu, Rui Dong, Deguang Kong, Juliette Burger, Anjelica Ramos, William Yang Wang, zhiheng huang, George Karypis, Bing Xiang and Dan Roth</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">The Impact of Symbolic Representations on In-context Learning for Few-shot Reasoning</span><br>
<span class="paper-authors">Hanlin Zhang, Yi-Fan Zhang, Li Erran Li, Eric Xing</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">The Magic of IF: Investigating Causal Reasoning Abilities in Large Language Models of Code</span><br>
<span class="paper-authors">Xiao Liu, Da Yin, Chen Zhang, Yansong Feng and Dongyan Zhao</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">The Role of Semantic Parsing in Understanding Procedural Text</span><br>
<span class="paper-authors">Hossein Rajaby Faghihi, Parisa Kordjamshidi, Choh Man Teng and James Allen</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>
</ul>

<h3>In-Person Poster Session 2</h3>
<ul class="paper-list">
<li>
<span class="paper-title">Beyond Vertical Thinking: Exploring and Quantifying Lateral Thinking in Pretrained Language Models</span><br>
<span class="paper-authors">Wenjuan Han, Yueting Yang Yijie Chen, Fandong Meng, Jie Zhou, Jinan Xu</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Can In-context Learners Learn a Reasoning Concept from Demonstrations?</span><br>
<span class="paper-authors">Michal Štefánik and Marek Kadlcik</span><br>
<span class="paper-type"><span style="color:#DD3333;font-weight:700">[Oral, Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Claim-Dissector: An Interpretable Fact-Checking System with Joint Re-ranking and Veracity Prediction</span><br>
<span class="paper-authors">Martin Fajcik, Petr Motlicek, Pavel Smrz</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Complementary Explanations for Effective In-Context Learning</span><br>
<span class="paper-authors">Xi Ye, Srinivasan Iyer, Asli Celikyilmaz, Veselin Stoyanov, Greg Durrett and Ramakanth Pasunuru</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Deductive Additivity for Planning of Natural Language Proofs</span><br>
<span class="paper-authors">Zayne Sprague, Kaj Bostrom, Swarat Chaudhuri and Greg Durrett</span><br>
<span class="paper-type"><span>[Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Distilling Reasoning Capabilities into Smaller Language Model</span><br>
<span class="paper-authors">Kumar Shridhar, Alessandro Stolfo, Mrinmaya Sachan</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes</span><br>
<span class="paper-authors">Cheng-Yu Hsieh, Chun-Liang Li, Chih-Kuah Yeh, Hootan Nakhost, Yasuhisa Fujii, Alex Ratner, Ranjay Krishna, Chen-Yu Lee and Tomas Pfister</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Explaining Competitive-Level Programming Solutions using LLMs</span><br>
<span class="paper-authors">Jierui Li, Szymon Tworkowski, Yingying Wu and Raymond Mooney</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Exploring the Curious Case of Code Prompts</span><br>
<span class="paper-authors">Li Zhang, Liam Dugan, Hainiu Xu and Chris Callison-Burch</span><br>
<span class="paper-type"><span style="color:#DD3333;font-weight:700">[Oral, Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Exploring the Effectiveness of Prompt Engineering for Legal Reasoning Tasks</span><br>
<span class="paper-authors">Fangyi Yu, Lee Quartey, Frank Schilder</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Faithful Chain-of-Thought Reasoning</span><br>
<span class="paper-authors">Qing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, Delip Rao, Eric Wong, Marianna Apidianaki and Chris Callison-Burch (lyuqing@seas.upenn.edu)</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Few Shot Rationale Generation using Self-Training with Dual Teachers</span><br>
<span class="paper-authors">Aditya Srikanth Veerubhotla, Lahari Poddar, Jun Yin, György Szarvas, Sharanya Eswaran</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Foveate, Attribute, and Rationalize: Towards Safe and Trustworthy AI</span><br>
<span class="paper-authors">Alex Mei, Sharon Levy, William Yang Wang</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Generative Multi-hop Retrieval</span><br>
<span class="paper-authors">Hyunji Lee, Sohee Yang, hanseok Oh and Minjoon Seo</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">HeGeL: A Novel Dataset for Hebrew Geo-Location</span><br>
<span class="paper-authors">Tzuf Paz-Argaman, Tal Bauman, Itai Mondshine, Itzhak Omer, Sagi Dalyot, Reut Tsarfaty</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">How Many Answers Should I Give? An Empirical Study of Multi-Answer Reading Comprehension</span><br>
<span class="paper-authors">Chen Zhang, Jiuheng Lin, Xiao Liu, Yuxuan Lai, Yansong Feng, Dongyan Zhao</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Knowledge Graph-augmented Language Models for Complex Question Answering</span><br>
<span class="paper-authors">Priyanka Sen, Sandeep Mavadia and Amir Saffari</span><br>
<span class="paper-type"><span>[Archival]</span></span><br>

</li>

<li>
<span class="paper-title">LaSQuE: Improved Zero-Shot Classification from Explanations Through Quantifier Modeling and Curriculum Learning</span><br>
<span class="paper-authors">Sayan Ghosh, Rakesh R. Menon, Shashank Srivastava</span><br>
<span class="paper-type"><span>[ACL Findings]</span></span><br>

</li>

<li>
<span class="paper-title">Let's Sample Step-by-Step: Adaptive-Consistency for Efficient Reasoning with LLMs</span><br>
<span class="paper-authors">Pranjal Aggarwal, Aman Madaan, Yiming Yang and Mausam</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">SCOTT: Self-Consistent Chain-of-Thought Distillation</span><br>
<span class="paper-authors">Peifeng Wang, Zhengyang Wang, Zheng Li, Yifan Gao, Bing Yin and Xiang Ren</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Saliency Map Verbalization: Comparing Feature Importance Representations from Model-free and Instruction-based Methods</span><br>
<span class="paper-authors">Nils Feldhus, Leonhard Hennig, Maximilian Dustin Nasert, Christopher Ebert, Robert Schwarzenberg and Sebastian Möller (nils.feldhus@dfki.de)</span><br>
<span class="paper-type"><span>[Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Situated Natural Language Explanations</span><br>
<span class="paper-authors">Zining Zhu, Haoming Jiang, Jingfeng Yang, Sreyashi Nag, Chao Zhang, Jie Huang, Yifan Gao, Frank Rudzicz and Bing Yin (zining@cs.toronto.edu)	</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Using Planning to Improve Semantic Parsing of Instructional Texts</span><br>
<span class="paper-authors">Vanya Cohen and Raymond Mooney</span><br>
<span class="paper-type"><span style="color:#DD3333;font-weight:700">[Oral, Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Negated Complementary Commonsense using Large Language Models</span><br>
<span class="paper-authors">Navid Rezaei and Marek Reformat </span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>

<li>
<span class="paper-title">Towards Reasoning in Large Language Models: Survey, Implication, and Reflection</span><br>
<span class="paper-authors">Jie Huang and Kevin Chen-Chuan Chang</span><br>
<span class="paper-type"><span>[Non-Archival]</span></span><br>

</li>
</ul>


<hr />

<div class="col-xs-12"  id="dates">
    <h2>Important Dates</h2>  
</div>

<br>
<div class="row">
  <div class="col-xs-12">
    <table class="table table-striped">
      <tbody>
        <tr>
          <td>Paper Submission Deadline</td>
          <td><s>April 24, 2023</s> <b>May 3, 2023</b> (All deadlines are 11:59 PM AoE time.)</td>
        </tr>
        <tr>
          <td>Decision Notifications</td>
          <td><s>May 22, 2023</s> <b>May 29, 2023</b></td>
        </tr>
        <tr>
          <td>Camera Ready Paper Deadline</td>
          <td><s>June 6, 2023 (11:59 PM Pacific time)</s></td>
        </tr>
        <tr>
          <td>Workshop Date</td>
          <td>Thursday, 13 July 2023</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>


<hr />


<!-- Organizers -->
<div class="row" id="organizers">
  <div class="col-xs-12">
    <h2>Organizers</h2>
  </div>
</div>

<div class="row">
  <div class="col-xs-6 col-lg-3">
    <a href="https://www.cs.utexas.edu/~gdurrett//">
      <img class="people-pic" src="https://www.cs.utexas.edu/~gdurrett/photo.png">
    </a>
    <div class="people-name">
      <a href="https://www.cs.utexas.edu/~gdurrett/">Greg Durrett</a>
      <h6>University of Texas, Austin</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://allenai.org/team/bhavanad/">
      <img class="people-pic" src="https://images.ctfassets.net/wf5t1ptx352c/6W6eEkb6MMkoU8gYM8CWgW/d2f1d7519f70705caef84f2a5b1af39b/Bhavana-Dalvi.jpg">
    </a>
    <div class="people-name">
      <a href="https://allenai.org/team/bhavanad/">Bhavana Dalvi</a>
      <h6>Allen Institute for AI</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://www.jasonwei.net/">
      <img class="people-pic" src="https://miro.medium.com/max/2400/0*hXD0QnXdG8YVp2v3">
    </a>
    <div class="people-name">
      <a href="https://www.jasonwei.net/">Jason Wei</a>
      <h6>Google Brain</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://cognitiveai.org/">
      <img class="people-pic" src="http://cognitiveai.org/wp-content/uploads/2016/10/peter_tedx-300x300.jpg">
    </a>
    <div class="people-name">
      <a href="https://cognitiveai.org/">Peter Jansen</a>
      <h6>University of Arizona</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://dnr2.github.io/academic_website/">
      <img class="people-pic" src="https://dnr2.github.io/academic_website/images/profile.jpg">
    </a>
    <div class="people-name">
      <a href="https://dnr2.github.io/academic_website/">Danilo Ribeiro</a>
      <h6>Northwestern University</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://web.mit.edu/zyzzyva/www/academic.html">
      <img class="people-pic" src="https://web.mit.edu/zyzzyva/www/images/CathyWong_profile.png">
    </a>
    <div class="people-name">
      <a href="https://web.mit.edu/zyzzyva/www/academic.html">Lionel Wong</a>
      <h6>MIT</h6>
    </div>
  </div>
</div>



<div class="row" id="cfp">
  <div class="col-xs-12">
    <h2>Call for Papers</h2>
  </div>
</div>
<div class="row">
  <div class="col-xs-12">
    <p>
      We welcome submissions on all topics related to natural language reasoning or structured explanations, which might include:
    </p>
    <p>
  <ul>
  <li>Multi-step natural language reasoning;</li>
  <li>Structured explanations;</li>
  <li>Foundations of natural language reasoning;</li>
  <li>Applications of natural language reasoning;</li>
  <li>Knowledge retrieval for multi-step reasoning;</li>
  <li>Reasoning as programs;</li>
          </ul>
      </p>
      <p>With recent scaling of large pre-trained Transformer language models (LLMs), the scope of feasible NLP tasks has broadened, including tasks requiring increasingly complex reasoning. Although LLMs have shown remarkable performance, it is still unclear how to best elicit this reasoning and how the answers that models give follow from what they "know." This workshop aims to bring together a diverse set of perspectives and attempt to establish common ground for how various kinds of explanation structures can tackle a broad class of reasoning problems in natural language and beyond. As such, the workshop welcomes and covers a wide range of topics, including (non-exclusively):</p>
  
  <ul>
    <li><b>Multi-step natural language reasoning: </b>Solving reasoning problems, such as those involving abstract manipulations, has been a long-standing challenge in the field of artificial intelligence. Large language models have recently achieved a new state-of-the-art performance on many reasoning benchmarks, often with approaches only requiring prompting. Current research frontiers are exploring what kinds of explanation formats are most effective, how reasoning is most effectively broken down, how to get language models to plan their reasoning, and what resources can be used to improve reasoning capabilities of language models. Tasks include mathematical reasoning, logical reasoning, commonsense reasoning, and more.</li>
  <li><b>Structured explanations: </b>Explanations for these complex tasks are typically composed of two or more facts that are used to help the reasoning process while also providing a record of the path taken to arrive at an inference. What representations can be best used by inference algorithms to construct large explanations? Frontiers of research include exploring search algorithms over such representations, how to represent annotations at scale and continual learning models.</li>
  <li><b>Foundations of natural language reasoning: </b>Does the structured reasoning constitute a plausible (interpretable to humans) and faithful (true to the model's processes) explanation? Does perturbing the reasoning lead to correctly modified behavior?
Applications of natural language reasoning: New QA settings, language grounding, explainable diagnosis systems, theorem provers using natural language, reasoning for scientific discovery, and more.</li>
  <li><b>Knowledge retrieval for multi-step reasoning: </b>It has been shown that LLMs can store factual knowledge implicitly in their parameters, however, their ability to access and manipulate knowledge is still limited. Future avenues of research include effective methods to combine parametric and non-parametric knowledge for complex reasoning, conditioning  retrieval given intermediate reasoning context, retrieving better provenance for structured explanations.</li>
  <li><b>Reasoning as programs: </b>Another body of work within computational cognitive science and AI has formalized reasoning as inference over programs, building on classical views of human reasoning in a symbol-like language of thought and linguistic semantics with logical languages. Language models of code to produce structured reasoning for commonsense problems or other similar approaches are all in scope here.</li>
 </ul>
  </div>
</div>
<hr />
<!-- Submission -->
<div class="row" id="guidelines">
  <div class="col-xs-12">
    <h2>Submission Guidelines</h2>
  </div>
</div>
<div class="row">
    <div class="col-xs-12">
      <p>
      We welcome two types of papers: regular workshop papers and non-archival submissions. Only regular workshop papers will be included in the workshop proceedings. All submissions should be in PDF format and made through <a style="color:#2980b9;font-weight:400;" href=" https://softconf.com/acl2023/nl-reasoning/">Softconf</a>. In line with the ACL main conference policy, camera-ready versions of papers will be given one additional page of content.
        </p>
    <ul>
      <li><b>Regular workshop papers</b>: Authors should submit a paper up to <b>8 pages (both short and long papers are welcome)</b>, with unlimited pages for references, following the <a style="color:#2980b9;font-weight:400;" href="https://2023.aclweb.org/calls/main_conference/#paper-types-and-formats">ACL 2023 formatting requirements</a>. The reported research should be substantially original. All submissions will be reviewed in a single track, regardless of length. Accepted papers will be presented as posters by default, and best papers may be given the opportunity for a brief talk to introduce their work. Reviewing will be double-blind, and thus no author information should be included in the papers; self-reference that identifies the authors should be avoided or anonymised. Accepted papers will appear in the workshop proceedings.
</li>
      <li><b>Non-archival submissions</b>: We also solicit cross-submissions, i.e., papers on relevant topics that <i>have appeared</i> in other venues (e.g., workshop or conference papers at NLP, ML, or cognitive science venues, among others). Accepted papers will be presented at the workshop, with an indication of original venue, but will not be included in the workshop proceedings. Cross-submissions are ideal for related work which would benefit from exposure to the <b>NLReasoning</b> audience. Interested authors should submit their papers in PDF format through the <b>NLReasoning</b> Softconf website, with a note on the original venue. They will be reviewed in a <b>single-blind</b> fashion. Papers in this category do not need to follow the ACL format, and the submission length is determined by the original venue. The paper selection will be solely determined by the organizing committee.</li>
    </ul>
    <p>
        In addition, we welcome papers on relevant topics that are under review or to be submitted to other venues (including the ACL 2023 main conference). These papers must follow the regular workshop paper format and will not be included in the workshop proceedings. Papers in this category will be reviewed by workshop reviewers.</p>
   
   <p>
     <b>Note to authors: While you submit your paper through Softconf (<a style="color:#2980b9;font-weight:400;" href=" https://softconf.com/acl2023/nl-reasoning/">here</a>), please select the “Submission Type” properly based on the guidelines.
</b></p>
   <p>
   For questions about the submission guidelines, please contact workshop organizers via <a href="nl-reasoning@googlegroups.com">nl-reasoning@googlegroups.com</a>.

     </p>
      
</div>
</div>
<hr />
  
