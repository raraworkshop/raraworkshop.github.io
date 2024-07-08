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
        <p>
          With recent scaling of large pre-trained Transformer language models (LLMs), the scope of feasible NLP tasks has broadened. Significant recent work has focused on tasks that require some kind of natural language reasoning. A trajectory in question answering has led us from extraction-oriented datasets like SQuAD to “multi-hop” reasoning datasets like HotpotQA and StrategyQA. Although LLMs have shown remarkable performance on most NLP tasks, it is often unclear why their answers follow from what they know. To address this gap, a new class of explanation techniques has emerged which play an integral part in structuring the reasoning necessary to solve these datasets. For example, the chain-of-thought paradigm leverages explanations as vehicles for LLMs to mimic human reasoning processes. Entailment trees offer a way to ground multi-step reasoning in a collection of verifiable steps. Frameworks like SayCan bridge high-level planning in language and with low-level action trajectories. As a result, we see a confluence of methods blending explainable machine learning/NLP, classical AI (especially theorem proving), and cognitive science (how do humans structure explanations?). This workshop aims to bring together a diverse set of perspectives from these different traditions and attempt to establish common ground for how these various kinds of explanation structures can tackle a broad class of reasoning problems in natural language and beyond.
        </p>
    </div>
</div>

<br />

<hr />

<!-- Speakers -->
<div class="row" id="speakers">
  <div class="col-xs-12">
    <h2>Speakers</h2>
  </div>
</div>
<div class="row">
  <div class="col-xs-6 col-lg-3">
    <a href="https://www.cs.cmu.edu/~sherryw/">
      <img class="people-pic" src="{{ "/static/img/people/sherrywu.jpeg" | prepend:site.baseurl }}">
    </a>
    <div class="people-name">
      <a href="https://www.cs.cmu.edu/~sherryw/">Sherry Tongshuang Wu</a>
      <h6>Carnegie Mellon University</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://www.cs.princeton.edu/~karthikn/">
      <img class="people-pic" src="{{ "/static/img/people/karthikn.jpg" | prepend:site.baseurl }}">
    </a>
    <div class="people-name">
      <a href="https://www.cs.princeton.edu/~karthikn/">Karthik Narasimhan</a>
      <h6>Princeton University</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://web.stanford.edu/~icard/">
      <img class="people-pic" src="https://philosophy.stanford.edu/sites/philosophy/files/styles/hs_medium_square_360x360/public/media/image/TIcard-photo.jpg?h=e98ce842&itok=kSJ6I6Bl">
    </a>
    <div class="people-name">
      <a href="https://web.stanford.edu/~icard/">Thomas Icard</a>
      <h6>Stanford University</h6>
    </div>
  </div>
    <div class="col-xs-6 col-lg-3">
    <a href="https://lorraine333.github.io/">
      <img class="people-pic" src="{{ "/static/img/people/lorrianeli.jpg" | prepend:site.baseurl }}">
    </a>
    <div class="people-name">
      <a href="https://lorraine333.github.io/">Xiang Lorraine Li</a>
      <h6>University of Pittsburgh</h6>
    </div>
  </div>
</div>

<hr />

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
  <li>Knowledge retrieval for multi-step reasoning;</li>
  <li>Reasoning in interactive environments;</li>
  <li>Applications of natural language reasoning;</li>
  <li>Reasoning as programs;</li>
  <li>Neuro-symbolic reasoning;</li>
          </ul>
      </p>
      <p>With recent scaling of large pre-trained Transformer language models (LLMs), the scope of feasible NLP tasks has broadened, including tasks requiring increasingly complex reasoning. Although LLMs have shown remarkable performance, it is still unclear how to best elicit this reasoning and to what extent the answers that models give follow from what they “know.” This workshop aims to bring together a diverse set of perspectives and attempts to establish common ground for how various kinds of explanation structures can tackle a broad class of reasoning problems in natural language and beyond. As such, the workshop welcomes and covers a wide range of topics, including (non-exclusively):</p>
  
  <ul>
    <li><b>Multi-step natural language reasoning: </b>Solving reasoning problems, such as those involving abstract manipulations, has been a long-standing challenge in the field of artificial intelligence. Large language models have recently achieved a new state-of-the-art performance on many reasoning benchmarks, often with approaches only requiring prompting. Current research frontiers are exploring what kinds of explanation formats are most effective, how reasoning is most effectively broken down, how to get language models to plan their reasoning, and what resources can be used to improve reasoning capabilities of language models. Tasks include mathematical reasoning, logical reasoning, commonsense reasoning, and more.</li>
  <li><b>Structured explanations: </b>Explanations for these complex tasks are typically composed of two or more facts that are used to help guide the reasoning process while also providing a record of the path taken to arrive at an inference. What representations can be best used by inference algorithms to construct large explanations? Frontiers of research include exploring search algorithms over such representations, how to represent annotations at scale and continual learning models.</li>
  <li><b>Foundations of natural language reasoning: </b>Does the structured reasoning constitute a plausible (interpretable to humans) and faithful (true to the model's processes) explanation? Does perturbing the reasoning lead to correctly modified behavior?</li>
  <li><b>Knowledge retrieval for multi-step reasoning: </b>It has been shown that LLMs can store factual knowledge implicitly in their parameters, however, their ability to access and manipulate knowledge is still limited. Future avenues of research include effective methods to combine parametric and non-parametric knowledge for complex reasoning, conditioning retrieval given intermediate reasoning context, retrieving better provenance for structured explanations.</li>
  <li><b>Reasoning in interactive environments: </b>Interactive environments are becoming an increasingly popular method for evaluating reasoning where an agent observes the environment, then takes steps in that environment to accomplish some goal. Here, manner (i.e. how-to) explanations take the form of the list of actions the agent required to accomplish some goal, e.g., "how to boil water in a kitchen", "how to grow an apple tree", "how to book a flight and a hotel in LA".</li>
  <li><b>Applications of natural language reasoning: </b>New QA settings, language grounding, explainable diagnosis systems, theorem provers using natural language, reasoning for scientific discovery, and more.</li>
  <li><b>Reasoning as programs: </b>Another body of work within computational cognitive science and AI has formalized reasoning as inference over programs, building on classical views of human reasoning in a symbol-like language of thought and linguistic semantics with logical languages. Language models of code to produce structured reasoning for commonsense problems or other similar approaches are all in scope here.</li>
  <li><b>Neuro-symbolic reasoning: </b>Pockets of contemporary work have proposed reformulating natural language reasoning as proceeding via modular neurosymbolic systems. Here LLMs operate as declarative programmers, “translating” natural language into a formal specification, such as one accepted by a satisfiability solver, and explicit inference is offloaded to classical symbolic algorithms for planning, constraint satisfaction, or probabilistic simulation.</li>
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
      We welcome three types of papers: archival workshop papers, non-archival papers, and non-archival cross-submissions. Only regular workshop papers will be included in the workshop proceedings. <i>Regular workshop submissions (both archival and non-archival)</i> should be in PDF format and made through the <b>OpenReview website</b> set up for this workshop 
      <a style="color:#2980b9;font-weight:400;" href="https://openreview.net/group?id=aclweb.org/ACL/2024/Workshop/NLRSE#tab-your-consoles">(link)</a>. In line with the ACL main conference policy, camera-ready versions of regular workshop papers will be given one additional page of content. <i>Non-archival cross-submissions</i> should be made through the <b>form</b> <a style="color:#2980b9;font-weight:400;" href="https://forms.gle/BKn4bczXfaXN7GSg7">(link)</a>.
        </p>
    <ul>
      <li><b>Archival regular workshop papers: </b>
      <!-- Authors should submit a paper up to <b>8 pages (both short and long papers are welcome)</b>, with unlimited pages for references, following the <a style="color:#2980b9;font-weight:400;" href="https://2023.aclweb.org/calls/main_conference/#paper-types-and-formats">ACL 2023 formatting requirements</a>. The reported research should be substantially original. All submissions will be reviewed in a single track, regardless of length. Accepted papers will be presented as posters by default, and best papers may be given the opportunity for a brief talk to introduce their work. Reviewing will be double-blind, and thus no author information should be included in the papers; self-reference that identifies the authors should be avoided or anonymised. Accepted papers will appear in the workshop proceedings. -->
      Authors should submit a paper <b>up to 8 pages (both short and long papers are welcome)</b>, with unlimited pages for references, following the <a href="https://www.aclweb.org/adminwiki/index.php/ACL_Author_Guidelines" style="color:#2980b9;font-weight:400;">ACL author guidelines</a>. The reported research should be substantially original. All submissions will be reviewed in a single track, regardless of length. Accepted papers will be presented as posters by default, and best papers may be given the opportunity for a brief talk to introduce their work. Reviewing will be double-blind, and thus no author information should be included in the papers; self-reference that identifies the authors should be avoided or anonymised. Accepted papers will appear in the workshop proceedings. <b>Preference for oral presentation slots in the workshop will be given to archival papers</b>.</li>
      <li> <b> Non-archival regular workshop papers: </b> This is the same as the option above, but these papers will not appear in the proceedings and will typically only receive poster presentation slots. Non-archival submissions in this category will still undergo the review process. This is appropriate for nearly finished work that is intended for submission to another venue at a later date. </li>
      <li><b>Non-archival cross-submissions: </b> We also solicit cross-submissions, i.e., papers on relevant topics that <i>have already</i> appeared in other venues (e.g., workshop or conference papers at NLP, ML, or cognitive science venues, among others). Accepted papers will be presented at the workshop, with an indication of original venue, but will not be included in the workshop proceedings. Cross-submissions are ideal for related work which would benefit from exposure to the <b>NLReasoning</b> audience. Papers in this category do not need to follow the ACL format, and the submission length is determined by the original venue. The paper selection will be solely determined by the organizing committee in a non-blind fashion. These papers will typically receive poster presentation slots.</li>
    </ul>
    <p>
        In addition, we welcome papers on relevant topics that are <i>under review or to be submitted to </i> other venues (including the ACL 2024 main conference). These papers must follow the regular workshop paper format and will not be included in the workshop proceedings. Papers in this category will be reviewed by workshop reviewers.</p>
   
   <p>
     <b>Note to authors: For archival and non-archival regular workshop submissions, while you submit your paper through OpenReview (<a style="color:#2980b9;font-weight:400;" href="https://openreview.net/group?id=aclweb.org/ACL/2024/Workshop/NLRSE#tab-your-consoles">link</a>), please select the "Submission Type" properly based on the guidelines. For cross-submissions, please fill out this form (<a style="color:#2980b9;font-weight:400;" href="https://forms.gle/BKn4bczXfaXN7GSg7">link</a>) and do NOT submit through OpenReview.
</b></p>
   <p>
   For questions about the submission guidelines, please contact workshop organizers via <a href="nl-reasoning@googlegroups.com">nl-reasoning@googlegroups.com</a>.

     </p>
      
</div>
</div>
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
          <td>May 21, 2024 (All deadlines are 11:59 PM AoE time.)</td>
        </tr>
        <tr>
          <td>Decision Notifications</td>
          <td>June 17, 2024</td>
        </tr>
        <tr>
          <td>Camera Ready Paper Deadline</td>
          <td>July 1, 2024</td>
        </tr>
        <tr>
          <td>Workshop Date</td>
          <td>Aug 15, 2024</td>
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
      <h6>Amazon AWS</h6>
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
  <div class="col-xs-6 col-lg-3">
    <a href="https://xiye17.github.io/">
      <img class="people-pic" src="https://xiye17.github.io/avatar.jpg">
    </a>
    <div class="people-name">
      <a href="https://xiye17.github.io/">Xi Ye</a>
      <h6>University of Texas, Austin</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://wenting-zhao.github.io/">
      <img class="people-pic" src="https://avatars.githubusercontent.com/u/8762524?v=4">
    </a>
    <div class="people-name">
      <a href="https://wenting-zhao.github.io/">Wenting Zhao</a>
      <h6>Cornell University</h6>
    </div>
  </div>
  <div class="col-xs-6 col-lg-3">
    <a href="https://benlipkin.github.io/index.html">
      <img class="people-pic" src="https://benlipkin.github.io/assets/images/compressed-816x816.jpg">
    </a>
    <div class="people-name">
      <a href="https://benlipkin.github.io/index.html">Ben Lipkin</a>
      <h6>MIT</h6>
    </div>
  </div>
</div>
