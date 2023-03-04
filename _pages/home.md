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
      <img class="people-pic" src="https://cs.brown.edu/people/epavlick/profile-pic-circle.gif">
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
  <div class="col-xs-6 col-lg-3">
    <a href="https://fh295.github.io/">
      <img class="people-pic" src="https://github.com/fh295/fh295.github.io/blob/master/felixhill.jpg?raw=true">
    </a>
    <div class="people-name">
      <a href="https://fh295.github.io/">Felix Hill</a>
      <h6>DeepMind</h6>
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
  
<div class="col-xs-12">
    <h2>Important Dates</h2>  
</div>

<br>
<div class="row">
  <div class="col-xs-12">
    <table class="table table-striped">
      <tbody>
        <tr>
          <td>Paper Submission Deadline</td>
          <td>April 24, 2023 (All deadlines are 11:59 PM AoE time.)</td>
        </tr>
        <tr>
          <td>Decision Notifications</td>
          <td>May 22, 2023</td>
        </tr>
        <tr>
          <td>Camera Ready Paper Deadline</td>
          <td>June 6, 2023 (11:59 PM Pacific time)</td>
        </tr>
        <tr>
          <td>Workshop Date</td>
          <td>(TBD. ACL workshops will take place on July 13-14, 2023)</td>
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

