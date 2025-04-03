title: How I Built and Launched a Japanese Kanji Learning App Using Vibe Coding
Slug: vibe-coding-kanjimasterai
Email: adil.mouja@gmail.com
Date: 2025-04-03
Category: ai
Tags: ai, gpt4, japanese
Summary: This article details how I leveraged vibe coding and modern AI tools to build KanjiMaster.ai, transforming a twenty-year-old dream of creating a better way to learn Japanese Kanji into reality.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What's Vibe coding?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Vibe coding is an AI-assisted programming technique where developers describe tasks in natural language and AI generates the corresponding code. The term was officially coined by Andrej Karpathy in February 2025. It involves using tools like Cursor IDE with Anthropic's Claude Sonnet to rapidly develop applications by describing functionality in natural language."
    }
  }]
}
</script>

Twenty years ago, at 18, I moved from Morocco to Japan to pursue a degree in computer science at a Japanese university. My journey started with an intensive one-year Japanese course. Everything seemed manageable—except for Kanji (if you're not familiar with the Japanese writing system, check out [this guide](https://www.kanjimaster.ai/blog/japanese-writing-system-hiragana-katakana-kanji)).

Anyone who's learned Japanese knows the struggle. The thousands of characters, multiple readings, and nuanced meanings make Kanji incredibly challenging. Back then, I kept thinking:
<div style="text-align: center; font-style: italic; font-size: 1.2em; margin: 20px 0; padding: 10px; border-left: 4px solid #ccc;">
"There must be a better way to learn Kanji."
</div>
This wish stayed with me for two decades, patiently waiting for technology to catch up.

#The Spark: GPT-4 and My First Kanji App (2023)

In March 2023, OpenAI released GPT-4, and like many others, I was immediately intrigued. Given my background as a developer mainly in Python, data engineering, machine learning, and AI, I quickly experimented with GPT-4's API.
I built a simple Python and vanilla JavaScript app to auto-generate multiple-choice quizzes for Kanji characters. 

<br>

<div style="display:block;margin:auto;height:60%;width:60%">
  <img src="/images/kanji-gpt4/kanji-gpt4.gif">
</div>

<br>

To my surprise, it worked well. Encouraged by the results, I wrote about my experience [here](/posts/2023/10/kanji-gpt4/). 

The positive feedback convinced me the idea had great potential.Yet, it still felt like just a prototype. I wanted more.


# The Turning Point: Discovering Vibe Coding and Cursor (Summer 2024)
By mid-2024, "vibe coding"—an AI-assisted programming technique where developers describe tasks in natural language and AI generates the corresponding code—had started gaining popularity. The term was officially coined by Andrej Karpathy in February 2025.

<br>

<div style="display: flex; justify-content: center; width: 100%; max-width: 550px; margin: 0 auto;">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">There&#39;s a new kind of coding I call &quot;vibe coding&quot;, where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It&#39;s possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also I just talk to Composer with SuperWhisper…</p>&mdash; Andrej Karpathy (@karpathy) <a href="https://twitter.com/karpathy/status/1886192184808149383?ref_src=twsrc%5Etfw">February 2, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

<br>

Cursor IDE with Anthropic's Claude Sonnet, quickly became a preferred tool among developers exploring this innovative approach.

Despite my extensive Python and AI background, I had no real experience with modern JavaScript frameworks like React or Next.js. To quickly get up to speed, I took a 4-hour YouTube crash course on React and Next.js. This short course was surprisingly enough to grasp the key concepts and structure.
Feeling ready, I dove into building a full-fledged app: [KanjiMaster.ai](https://kanjimaster.ai/).

# Step 1: Defining the Tech Stack
Before diving into the implementation details, here's the tech stack I chose:

* Full-Stack Framework: [Next.js](https://nextjs.org/) – Modern React framework for building performant, SEO-friendly web applications.
* Database: [Supabase](https://supabase.com/) – Open-source Firebase alternative built on PostgreSQL, providing easy database management and built-in APIs.
* Authentication: [Supabase Auth](https://supabase.com/docs/guides/auth) – seamless integration, supporting Google login and passwordless email-based login.
* Payments & Subscriptions: [Stripe](https://stripe.com/) – Reliable and secure handling of subscriptions and payments.
* Transactional Emails: [Resend](https://resend.com/) – Simple and effective email delivery for user communications.
* Analytics & Product Insights: [PostHog](https://posthog.com/) – Open-source analytics to monitor user behavior and app usage.
* Hosting & Deployment: [Vercel](https://vercel.com/) – Fast, scalable, and effortless deployment optimized specifically for Next.js.
* Development IDE: [Cursor](http://cursor.com/) – AI-powered IDE for fast, efficient vibe coding.

<div style="display:block;margin:auto;height:100%;width:100%">
  <img src="/images/vibe-coding-kanjimasterai/technology_stack.png">
</div>

This carefully selected stack allowed me to iterate quickly and efficiently, enabling a solo developer like myself to manage the entire product lifecycle from inception to launch.

# Step 2: Generating High-Quality Kanji Data with GPT-4o

I started by generating robust content. I extracted [the Jōyō Kanji list](https://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji) from Wikipedia and enriched it using GPT-4o. Using Python scripts, I asked GPT-4o to generate detailed structured data for each Kanji:

* On'yomi and Kun'yomi readings
* Example sentences
* Difficulty ratings & JLPT levels
* Word distractors for quizzes
* ...

Example Python prompt:

```python
prompt = PromptTemplate(
    template="""Generate detailed information about the kanji {kanji}.
    Provide comprehensive information in the following JSON format:
    {{
        "kanji": "{kanji}",
        "radical": "string (the primary radical component)",
        "strokes": integer (number of strokes),
        "jlpt_level": "string (JLPT Level)",
        "grade_level": integer (1-6 for elementary school grades, 7 for secondary school),
        "meaning": "string (English meaning)",
        "onyomi": "string (katakana readings)",
        "kunyomi": "string (hiragana readings)",
        "onyomi_romaji": "string (romaji of onyomi)",
        "kunyomi_romaji": "string (romaji of kunyomi)",
    }}""",
    input_variables=["kanji"]
)
```

Though GPT-4o's results were excellent, I did manual spot-checking to ensure quality, iterating and refining until the data felt strong enough for initial launch. Below are example of a Kanji and a Kanji Compound from the database.

<div style="display:block;margin:auto;height:90%;width:90%">
  <img src="/images/vibe-coding-kanjimasterai/Kanji_compound.png">
</div>

#Step 3: Designing Clear Data Models and APIs

Thanks to my background, designing the data models, database schema (using Supabase/Postgres), and API structure came naturally. This solid foundation was crucial for the AI-driven development that followed.

My initial app requirements included:

* Kanji and Kanji Compounds dictionary
* Kanji Collections
* Lessons
* Quizzes
* User profiles with progress tracking
* Payments and subscriptions (Stripe integration)
* Secure authentication (Supabase Auth)

# Step 4: Building KanjiMaster.ai using vibe coding 
Using Cursor IDE, I described the desired functionality clearly in natural language, and GPT handled the rest, generating roughly 95% of the code.

Example vibe coding comments:

```bash
Generate a dashboard that takes as input quizzes data for a specific user and displays key metrics, such as Learning Streak, Number of Kanji Mastered, and Number of Quizzes Taken. Retrieve available tables using Supabase MCP, and refer to the API folder to identify suitable APIs for this task.
```

Cursor generated reliable, performant code with minimal manual intervention, significantly accelerating my development process.

Below are a few screenshots of the final product.

<div style="display:block;margin:auto;width:90%;margin-top:20px;margin-bottom:20px;">
  <div style="text-align:center;margin-bottom:10px;font-style:italic;">Scroll horizontally to view all screenshots →</div>
  <div style="display:flex;overflow-x:scroll;gap:15px;padding:10px;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;">
    <img src="/images/vibe-coding-kanjimasterai/screenshot_1.png" style="width:100%;max-width:600px;scroll-snap-align:start;border-radius:8px;box-shadow:0 4px 8px rgba(0,0,0,0.1);">
    <img src="/images/vibe-coding-kanjimasterai/screenshot_2.png" style="width:100%;max-width:600px;scroll-snap-align:start;border-radius:8px;box-shadow:0 4px 8px rgba(0,0,0,0.1);">
    <img src="/images/vibe-coding-kanjimasterai/screenshot_3.png" style="width:100%;max-width:600px;scroll-snap-align:start;border-radius:8px;box-shadow:0 4px 8px rgba(0,0,0,0.1);">
    <img src="/images/vibe-coding-kanjimasterai/screenshot_4.png" style="width:100%;max-width:600px;scroll-snap-align:start;border-radius:8px;box-shadow:0 4px 8px rgba(0,0,0,0.1);">
  </div>
  <div style="text-align:center;margin-top:10px;color:#666;">Scroll horizontally to view all screenshots →</div>
</div>

### Debugging and the Importance of Structured Logs

Initially, debugging via Cursor felt like magic, but I quickly learned that clarity was key. Sometimes, I'd lazily paste logs into Cursor, expecting miracles—this often failed.

However, when I structured my debugging process, simplified the problem, and provided clear, minimal logs, Cursor became incredibly effective. Systematic debugging made AI assistance immensely productive.

#Step 5: Deploying Seamlessly to Vercel

When it came to deployment, I chose Vercel. The experience was seamless—I simply connected my GitHub repository, and within minutes, my Next.js app was live with automatic deployments and a scalable serverless architecture. The effortless deployment process allowed me to focus entirely on product development and iteration.



#Step 6: Launching and Early Marketing Strategy
Months before launch, I secured the domain KanjiMaster.ai, established social media presence (particularly [Instagram](https://www.instagram.com/kanjimasterai/)), and began producing AI-driven content to build a small community. I set up a simple landing page and collected emails organically, aided by a modest ad campaign (~$50). Below is a screenshot from the @kanjimasterai Instagram account.

<br>

<div style="display:block;margin:auto;height:100%;width:100%">
  <img src="/images/vibe-coding-kanjimasterai/ig.png">
</div>

<br>

[KanjiMaster.ai](https://www.kanjimaster.ai/) launched with content structured into five distinct Kanji collections, each aligned with the JLPT (Japanese Language Proficiency Test) levels. I adopted a freemium model:

* Free Tier: Full access to JLPT N5 (the easiest Kanji)
* Premium Tier: Complete access to all collections (JLPT N4 to N1)
    * Pricing: \$9.99/month or \$99.99/year
    * Included a 7-day free trial for premium content.

<div style="display:block;margin:auto;height:100%;width:100%">
  <img src="/images/vibe-coding-kanjimasterai/pricing.png">
</div>

<br>

Upon launch, I emailed my subscriber list, posted across social media, which quickly generated initial traction.

###One Month Post-Launch Stats:

* 120 total users (primarily organic)
* A handful of paying subscribers (mostly supportive friends)
* Steady organic traffic from SEO-driven content. I published my first blog post ["The Japanese Writing System Explained: Hiragana, Katakana & Kanji"](https://www.kanjimaster.ai/blog/japanese-writing-system-hiragana-katakana-kanji) which did well on Hacker News and generated some traffic.

#Step 7: Post-Launch Enhancements (Internal Admin Tools)

After deployment, managing users and data efficiently became essential. To streamline this, I built two internal admin apps (also via vibe coding):

1. CRM App: Managed interactions, user feedback, and communication logs, significantly enhancing customer support and user engagement.
2. Data Management App: Allowed easy corrections of Kanji data, dramatically reducing iteration time for content improvements.

These internal tools became indispensable for maintaining quality and staying closely connected with users post-launch.


<div style="display:block;margin:auto;width:90%;margin-top:20px;margin-bottom:20px;">
  <div style="text-align:center;margin-bottom:10px;font-style:italic;">Scroll horizontally to view all screenshots →</div>
  <div style="display:flex;overflow-x:scroll;gap:15px;padding:10px;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;">
    <img src="/images/vibe-coding-kanjimasterai/screenshot_5.jpeg" style="width:100%;max-width:600px;scroll-snap-align:start;border-radius:8px;box-shadow:0 4px 8px rgba(0,0,0,0.1);">
    <img src="/images/vibe-coding-kanjimasterai/screenshot_6.png" style="width:100%;max-width:600px;scroll-snap-align:start;border-radius:8px;box-shadow:0 4px 8px rgba(0,0,0,0.1);">
    <img src="/images/vibe-coding-kanjimasterai/screenshot_7.png" style="width:100%;max-width:600px;scroll-snap-align:start;border-radius:8px;box-shadow:0 4px 8px rgba(0,0,0,0.1);">
  </div>
  <div style="text-align:center;margin-top:10px;color:#666;">Scroll horizontally to view all screenshots →</div>
</div>



#Recommendations for Effective Vibe Coding:

For developers interested in leveraging vibe coding and AI effectively, here's my advice:

1.**Master the fundamentals first**: Before diving into vibe coding, ensure you understand:

  * How web applications work (client-server architecture)
  * Database concepts and data modeling
  * Authentication and security principles
  * API design and REST principles
  * Basic front-end concepts (DOM, state management, routing)

2.**Understand your tech stack thoroughly**: 

  * Know what each component does (e.g., Next.js for SSR/routing, Supabase for backend/auth)
  * Learn the core concepts of your main framework (4 hours was sufficient for React & Next.js basics)
  * Research and choose tools that work well together
  * Stay updated with best practices for each technology

3.**Focus on architecture and integration**:

  * Plan how different pieces will work together
  * Design clear data flows between components
  * Consider scalability and maintainability from the start

4.**Optimize your AI interactions**:

  * Provide clear context about your tech stack and constraints
  * Break complex features into smaller, focused tasks
  * Systematic debugging with clear, structured logs

For specific tips on working with Cursor effectively, this advice from @ericzakariasson captures it well:

<div style="display: flex; justify-content: center; width: 100%; max-width: 550px; margin: 20px auto;">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Some tips for working effectively with Cursor:<br><br>1. Be specific about the tech stack and any constraints<br>2. Break down complex features into smaller tasks<br>3. Review and understand the generated code<br>4. Keep track of your architecture decisions<br><br>The more context you provide, the better the results.</p>&mdash; Eric Zakariasson (@ericzakariasson) <a href="https://twitter.com/ericzakariasson/status/1906820861568442564">September 26, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

#Lessons Learned and Next Steps

Key insights from launching KanjiMaster.ai:

* AI drastically lowers the barrier to adopting new tech stacks.
* Pre-launch marketing and community building significantly boost launch success.
* Freemium conversion requires continual refinement and deep user engagement.
* Robust internal tooling drastically improves post-launch productivity.

My immediate next steps include direct user engagement, refining product-market fit, and continuously improving content quality and SEO.

#Wrapping Up: Realizing a Twenty-Year-Old Dream

Two decades ago, I struggled deeply with Kanji learning. Today, leveraging AI, vibe coding, a modern tech stack, KanjiMaster.ai has finally become a reality.

By sharing my journey, I hope it encourages you to revisit your own long-held ideas—today's tools might finally make them achievable.

Explore [KanjiMaster.ai](https://kanjimaster.ai/), or feel free to reach out — I'd love your thoughts and feedback!
