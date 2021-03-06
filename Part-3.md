<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="ROBOTS" content="ALL" />
    <meta http-equiv="imagetoolbar" content="no" />
    <meta name="MSSmartTagsPreventParsing" content="true" />
    <meta name="Copyright" content="Django Software Foundation" />
    <meta name="keywords" content="Python, Django, framework, open-source" />
    <meta name="description" content="" />

    <!-- Favicons -->
    <link rel="apple-touch-icon" href="/s/img/icon-touch.e4872c4da341.png">
    <link rel="icon" sizes="192x192" href="/s/img/icon-touch.e4872c4da341.png">
    <link rel="shortcut icon" href="/s/img/favicon.6dbf28c0650e.ico">
    <meta name="msapplication-TileColor" content="#113228">
    <meta name="msapplication-TileImage" content="/s/img/icon-tile.b01ac0ef9f67.png">

    <title>Writing your first Django app, part 3 | Django documentation | Django</title>

    <link rel="stylesheet" href="/s/css/output.979a53253070.css" >
    <script src="/s/js/lib/webfontloader/webfontloader.e75218f5f090.js"></script>
    <script>
    WebFont.load({
      custom: {
        families: ['FontAwesome', 'Fira+Mono'],
      },
      google: {
        families: ['Roboto:400italic,700italic,300,700,400:latin'
        ]
      },
      classes: false,
      events: false,
      timeout: 1000
    });
    </script>
    <script src="/s/js/lib/modernizr.3b36762e418a.js"></script>
    
  
    
      
    
  
  <link rel="canonical" href="https://docs.djangoproject.com/en/1.11/intro/tutorial03/">
  
    
        
          
        
        
        <link rel="alternate"
           hreflang="el"
           href="https://docs.djangoproject.com/el/1.11/intro/tutorial03/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="x-default"
           href="https://docs.djangoproject.com/en/1.11/intro/tutorial03/">
        
        <link rel="alternate"
           hreflang="en"
           href="https://docs.djangoproject.com/en/1.11/intro/tutorial03/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="es"
           href="https://docs.djangoproject.com/es/1.11/intro/tutorial03/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="fr"
           href="https://docs.djangoproject.com/fr/1.11/intro/tutorial03/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="id"
           href="https://docs.djangoproject.com/id/1.11/intro/tutorial03/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="ja"
           href="https://docs.djangoproject.com/ja/1.11/intro/tutorial03/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="pl"
           href="https://docs.djangoproject.com/pl/1.11/intro/tutorial03/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="pt-br"
           href="https://docs.djangoproject.com/pt-br/1.11/intro/tutorial03/">
    
  

  <link rel="search"
        type="application/opensearchdescription+xml"
        href="https://docs.djangoproject.com/en/1.11/search/description/"
        title="Django documentation">

  </head>

  <body id="generic" class="">

    <div role="banner" id="top">
  <div class="container">
    <a class="logo" href="https://www.djangoproject.com/">Django</a>
    <p class="meta">The web framework for perfectionists with deadlines.</p>
    <div role="navigation">
      <ul>
        <li>
          <a href="https://www.djangoproject.com/start/overview/">Overview</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/download/">Download</a>
        </li>
        <li class="active">
          <a href="https://docs.djangoproject.com/">Documentation</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/weblog/">News</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/community/">Community</a>
        </li>
        <li>
          <a href="https://code.djangoproject.com/">Code</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/foundation/">About</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/fundraising/">&#9829; Donate</a>
        </li>
      </ul>
    </div>
  </div>
</div>


    <div class="copy-banner">
      <div class="container">
        
  <h1><a href="https://docs.djangoproject.com/en/1.11/">Documentation</a></h1>

      </div>
    </div>
    <div id="billboard"></div>

    <div class="container sidebar-right">
      <div role="main">

        
          
        

        
<div id="version-switcher">
  <ul id="doc-languages" class="language-switcher">
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/el/1.11/intro/tutorial03/">el</a>
  </li>
  
  
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/es/1.11/intro/tutorial03/">es</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/fr/1.11/intro/tutorial03/">fr</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/id/1.11/intro/tutorial03/">id</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/ja/1.11/intro/tutorial03/">ja</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/pl/1.11/intro/tutorial03/">pl</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/pt-br/1.11/intro/tutorial03/">pt-br</a>
  </li>
  
  
    <li class="current"
        title="Click on the links on the left to switch to another language.">
      <span>Language: <strong>en</strong></span>
    </li>
  </ul>

  
  <ul id="doc-versions" class="version-switcher">
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.7/intro/tutorial03/">1.7</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.8/intro/tutorial03/">1.8</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.9/intro/tutorial03/">1.9</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.10/intro/tutorial03/">1.10</a>
    </li>
    
    
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/dev/intro/tutorial03/">dev</a>
    </li>
    
    
    <li class="current"
        title="This document describes Django 1.11. Click on the links on the left to see other versions.">
       <span>Documentation version:
         <strong>1.11</strong>
       </span>
    </li>
  </ul>
</div>


<div id="docs-content">
<div class="section" id="s-writing-your-first-django-app-part-3">
<span id="writing-your-first-django-app-part-3"></span><h1>Writing your first Django app, part 3<a class="headerlink" href="#writing-your-first-django-app-part-3" title="Permalink to this headline">¶</a></h1>
<p>This tutorial begins where <a class="reference internal" href="../tutorial02/"><span class="doc">Tutorial 2</span></a> left off. We&#8217;re
continuing the Web-poll application and will focus on creating the public
interface &#8211; &#8220;views.&#8221;</p>
<div class="section" id="s-overview">
<span id="overview"></span><h2>Overview<a class="headerlink" href="#overview" title="Permalink to this headline">¶</a></h2>
<p>A view is a &#8220;type&#8221; of Web page in your Django application that generally serves
a specific function and has a specific template. For example, in a blog
application, you might have the following views:</p>
<ul class="simple">
<li>Blog homepage &#8211; displays the latest few entries.</li>
<li>Entry &#8220;detail&#8221; page &#8211; permalink page for a single entry.</li>
<li>Year-based archive page &#8211; displays all months with entries in the
given year.</li>
<li>Month-based archive page &#8211; displays all days with entries in the
given month.</li>
<li>Day-based archive page &#8211; displays all entries in the given day.</li>
<li>Comment action &#8211; handles posting comments to a given entry.</li>
</ul>
<p>In our poll application, we&#8217;ll have the following four views:</p>
<ul class="simple">
<li>Question &#8220;index&#8221; page &#8211; displays the latest few questions.</li>
<li>Question &#8220;detail&#8221; page &#8211; displays a question text, with no results but
with a form to vote.</li>
<li>Question &#8220;results&#8221; page &#8211; displays results for a particular question.</li>
<li>Vote action &#8211; handles voting for a particular choice in a particular
question.</li>
</ul>
<p>In Django, web pages and other content are delivered by views. Each view is
represented by a simple Python function (or method, in the case of class-based
views). Django will choose a view by examining the URL that&#8217;s requested (to be
precise, the part of the URL after the domain name).</p>
<p>Now in your time on the web you may have come across such beauties as
&#8220;ME2/Sites/dirmod.asp?sid=&amp;type=gen&amp;mod=Core+Pages&amp;gid=A6CD4967199A42D9B65B1B&#8221;.
You will be pleased to know that Django allows us much more elegant
<em>URL patterns</em> than that.</p>
<p>A URL pattern is simply the general form of a URL - for example:
<code class="docutils literal"><span class="pre">/newsarchive/&lt;year&gt;/&lt;month&gt;/</span></code>.</p>
<p>To get from a URL to a view, Django uses what are known as &#8216;URLconfs&#8217;. A
URLconf maps URL patterns (described as regular expressions) to views.</p>
<p>This tutorial provides basic instruction in the use of URLconfs, and you can
refer to <a class="reference internal" href="../../ref/urlresolvers/#module-django.urls" title="django.urls"><code class="xref py py-mod docutils literal"><span class="pre">django.urls</span></code></a> for more information.</p>
</div>
<div class="section" id="s-writing-more-views">
<span id="writing-more-views"></span><h2>Writing more views<a class="headerlink" href="#writing-more-views" title="Permalink to this headline">¶</a></h2>
<p>Now let&#8217;s add a few more views to <code class="docutils literal"><span class="pre">polls/views.py</span></code>. These views are
slightly different, because they take an argument:</p>
<div class="highlight-default snippet"><div class="snippet-filename">polls/views.py</div>
<div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">detail</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">question_id</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="s2">&quot;You&#39;re looking at question </span><span class="si">%s</span><span class="s2">.&quot;</span> <span class="o">%</span> <span class="n">question_id</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">results</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">question_id</span><span class="p">):</span>
    <span class="n">response</span> <span class="o">=</span> <span class="s2">&quot;You&#39;re looking at the results of question </span><span class="si">%s</span><span class="s2">.&quot;</span>
    <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="n">response</span> <span class="o">%</span> <span class="n">question_id</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">vote</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">question_id</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="s2">&quot;You&#39;re voting on question </span><span class="si">%s</span><span class="s2">.&quot;</span> <span class="o">%</span> <span class="n">question_id</span><span class="p">)</span>
</pre></div>
</div>
<p>Wire these new views into the <code class="docutils literal"><span class="pre">polls.urls</span></code> module by adding the following
<a class="reference internal" href="../../ref/urls/#django.conf.urls.url" title="django.conf.urls.url"><code class="xref py py-func docutils literal"><span class="pre">url()</span></code></a> calls:</p>
<div class="highlight-default snippet"><div class="snippet-filename">polls/urls.py</div>
<div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">django.conf.urls</span> <span class="k">import</span> <span class="n">url</span>

<span class="kn">from</span> <span class="nn">.</span> <span class="k">import</span> <span class="n">views</span>

<span class="n">urlpatterns</span> <span class="o">=</span> <span class="p">[</span>
    <span class="c1"># ex: /polls/</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^$&#39;</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">index</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;index&#39;</span><span class="p">),</span>
    <span class="c1"># ex: /polls/5/</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^(?P&lt;question_id&gt;[0-9]+)/$&#39;</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">detail</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;detail&#39;</span><span class="p">),</span>
    <span class="c1"># ex: /polls/5/results/</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^(?P&lt;question_id&gt;[0-9]+)/results/$&#39;</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">results</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;results&#39;</span><span class="p">),</span>
    <span class="c1"># ex: /polls/5/vote/</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^(?P&lt;question_id&gt;[0-9]+)/vote/$&#39;</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">vote</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;vote&#39;</span><span class="p">),</span>
<span class="p">]</span>
</pre></div>
</div>
<p>Take a look in your browser, at &#8220;/polls/34/&#8221;. It&#8217;ll run the <code class="docutils literal"><span class="pre">detail()</span></code>
method and display whatever ID you provide in the URL. Try
&#8220;/polls/34/results/&#8221; and &#8220;/polls/34/vote/&#8221; too &#8211; these will display the
placeholder results and voting pages.</p>
<p>When somebody requests a page from your website &#8211; say, &#8220;/polls/34/&#8221;, Django
will load the <code class="docutils literal"><span class="pre">mysite.urls</span></code> Python module because it&#8217;s pointed to by the
<a class="reference internal" href="../../ref/settings/#std:setting-ROOT_URLCONF"><code class="xref std std-setting docutils literal"><span class="pre">ROOT_URLCONF</span></code></a> setting. It finds the variable named <code class="docutils literal"><span class="pre">urlpatterns</span></code>
and traverses the regular expressions in order. After finding the match at
<code class="docutils literal"><span class="pre">'^polls/'</span></code>, it strips off the matching text (<code class="docutils literal"><span class="pre">&quot;polls/&quot;</span></code>) and sends the
remaining text &#8211; <code class="docutils literal"><span class="pre">&quot;34/&quot;</span></code> &#8211; to the &#8216;polls.urls&#8217; URLconf for further
processing. There it matches <code class="docutils literal"><span class="pre">r'^(?P&lt;question_id&gt;[0-9]+)/$'</span></code>, resulting in a
call to the <code class="docutils literal"><span class="pre">detail()</span></code> view like so:</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="n">detail</span><span class="p">(</span><span class="n">request</span><span class="o">=&lt;</span><span class="n">HttpRequest</span> <span class="nb">object</span><span class="o">&gt;</span><span class="p">,</span> <span class="n">question_id</span><span class="o">=</span><span class="s1">&#39;34&#39;</span><span class="p">)</span>
</pre></div>
</div>
<p>The <code class="docutils literal"><span class="pre">question_id='34'</span></code> part comes from <code class="docutils literal"><span class="pre">(?P&lt;question_id&gt;[0-9]+)</span></code>. Using parentheses
around a pattern &#8220;captures&#8221; the text matched by that pattern and sends it as an
argument to the view function; <code class="docutils literal"><span class="pre">?P&lt;question_id&gt;</span></code> defines the name that will
be used to identify the matched pattern; and <code class="docutils literal"><span class="pre">[0-9]+</span></code> is a regular expression to
match a sequence of digits (i.e., a number).</p>
<p>Because the URL patterns are regular expressions, there really is no limit on
what you can do with them. And there&#8217;s no need to add URL cruft such as
<code class="docutils literal"><span class="pre">.html</span></code> &#8211; unless you want to, in which case you can do something like
this:</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^polls/latest\.html$&#39;</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">index</span><span class="p">),</span>
</pre></div>
</div>
<p>But, don&#8217;t do that. It&#8217;s silly.</p>
</div>
<div class="section" id="s-write-views-that-actually-do-something">
<span id="write-views-that-actually-do-something"></span><h2>Write views that actually do something<a class="headerlink" href="#write-views-that-actually-do-something" title="Permalink to this headline">¶</a></h2>
<p>Each view is responsible for doing one of two things: returning an
<a class="reference internal" href="../../ref/request-response/#django.http.HttpResponse" title="django.http.HttpResponse"><code class="xref py py-class docutils literal"><span class="pre">HttpResponse</span></code></a> object containing the content for the
requested page, or raising an exception such as <a class="reference internal" href="../../topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a>. The
rest is up to you.</p>
<p>Your view can read records from a database, or not. It can use a template
system such as Django&#8217;s &#8211; or a third-party Python template system &#8211; or not.
It can generate a PDF file, output XML, create a ZIP file on the fly, anything
you want, using whatever Python libraries you want.</p>
<p>All Django wants is that <a class="reference internal" href="../../ref/request-response/#django.http.HttpResponse" title="django.http.HttpResponse"><code class="xref py py-class docutils literal"><span class="pre">HttpResponse</span></code></a>. Or an exception.</p>
<p>Because it&#8217;s convenient, let&#8217;s use Django&#8217;s own database API, which we covered
in <a class="reference internal" href="../tutorial02/"><span class="doc">Tutorial 2</span></a>. Here&#8217;s one stab at a new <code class="docutils literal"><span class="pre">index()</span></code>
view, which displays the latest 5 poll questions in the system, separated by
commas, according to publication date:</p>
<div class="highlight-default snippet"><div class="snippet-filename">polls/views.py</div>
<div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">django.http</span> <span class="k">import</span> <span class="n">HttpResponse</span>

<span class="kn">from</span> <span class="nn">.models</span> <span class="k">import</span> <span class="n">Question</span>


<span class="k">def</span> <span class="nf">index</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
    <span class="n">latest_question_list</span> <span class="o">=</span> <span class="n">Question</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="s1">&#39;-pub_date&#39;</span><span class="p">)[:</span><span class="mi">5</span><span class="p">]</span>
    <span class="n">output</span> <span class="o">=</span> <span class="s1">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">q</span><span class="o">.</span><span class="n">question_text</span> <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">latest_question_list</span><span class="p">])</span>
    <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>

<span class="c1"># Leave the rest of the views (detail, results, vote) unchanged</span>
</pre></div>
</div>
<p>There&#8217;s a problem here, though: the page&#8217;s design is hard-coded in the view. If
you want to change the way the page looks, you&#8217;ll have to edit this Python code.
So let&#8217;s use Django&#8217;s template system to separate the design from Python by
creating a template that the view can use.</p>
<p>First, create a directory called <code class="docutils literal"><span class="pre">templates</span></code> in your <code class="docutils literal"><span class="pre">polls</span></code> directory.
Django will look for templates in there.</p>
<p>Your project&#8217;s <a class="reference internal" href="../../ref/settings/#std:setting-TEMPLATES"><code class="xref std std-setting docutils literal"><span class="pre">TEMPLATES</span></code></a> setting describes how Django will load and
render templates. The default settings file configures a <code class="docutils literal"><span class="pre">DjangoTemplates</span></code>
backend whose <a class="reference internal" href="../../ref/settings/#std:setting-TEMPLATES-APP_DIRS"><code class="xref std std-setting docutils literal"><span class="pre">APP_DIRS</span></code></a> option is set to
<code class="docutils literal"><span class="pre">True</span></code>. By convention <code class="docutils literal"><span class="pre">DjangoTemplates</span></code> looks for a &#8220;templates&#8221;
subdirectory in each of the <a class="reference internal" href="../../ref/settings/#std:setting-INSTALLED_APPS"><code class="xref std std-setting docutils literal"><span class="pre">INSTALLED_APPS</span></code></a>.</p>
<p>Within the <code class="docutils literal"><span class="pre">templates</span></code> directory you have just created, create another
directory called <code class="docutils literal"><span class="pre">polls</span></code>, and within that create a file called
<code class="docutils literal"><span class="pre">index.html</span></code>. In other words, your template should be at
<code class="docutils literal"><span class="pre">polls/templates/polls/index.html</span></code>. Because of how the <code class="docutils literal"><span class="pre">app_directories</span></code>
template loader works as described above, you can refer to this template within
Django simply as <code class="docutils literal"><span class="pre">polls/index.html</span></code>.</p>
<div class="admonition-template-namespacing admonition">
<p class="first admonition-title">Template namespacing</p>
<p class="last">Now we <em>might</em> be able to get away with putting our templates directly in
<code class="docutils literal"><span class="pre">polls/templates</span></code> (rather than creating another <code class="docutils literal"><span class="pre">polls</span></code> subdirectory),
but it would actually be a bad idea. Django will choose the first template
it finds whose name matches, and if you had a template with the same name
in a <em>different</em> application, Django would be unable to distinguish between
them. We need to be able to point Django at the right one, and the easiest
way to ensure this is by <em>namespacing</em> them. That is, by putting those
templates inside <em>another</em> directory named for the application itself.</p>
</div>
<p>Put the following code in that template:</p>
<div class="highlight-html+django snippet"><div class="snippet-filename">polls/templates/polls/index.html</div>
<div class="highlight"><pre><span></span><span class="cp">{%</span> <span class="k">if</span> <span class="nv">latest_question_list</span> <span class="cp">%}</span>
    <span class="p">&lt;</span><span class="nt">ul</span><span class="p">&gt;</span>
    <span class="cp">{%</span> <span class="k">for</span> <span class="nv">question</span> <span class="k">in</span> <span class="nv">latest_question_list</span> <span class="cp">%}</span>
        <span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;/polls/</span><span class="cp">{{</span> <span class="nv">question.id</span> <span class="cp">}}</span><span class="s">/&quot;</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
    <span class="cp">{%</span> <span class="k">endfor</span> <span class="cp">%}</span>
    <span class="p">&lt;/</span><span class="nt">ul</span><span class="p">&gt;</span>
<span class="cp">{%</span> <span class="k">else</span> <span class="cp">%}</span>
    <span class="p">&lt;</span><span class="nt">p</span><span class="p">&gt;</span>No polls are available.<span class="p">&lt;/</span><span class="nt">p</span><span class="p">&gt;</span>
<span class="cp">{%</span> <span class="k">endif</span> <span class="cp">%}</span>
</pre></div>
</div>
<p>Now let&#8217;s update our <code class="docutils literal"><span class="pre">index</span></code> view in <code class="docutils literal"><span class="pre">polls/views.py</span></code> to use the template:</p>
<div class="highlight-default snippet"><div class="snippet-filename">polls/views.py</div>
<div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">django.http</span> <span class="k">import</span> <span class="n">HttpResponse</span>
<span class="kn">from</span> <span class="nn">django.template</span> <span class="k">import</span> <span class="n">loader</span>

<span class="kn">from</span> <span class="nn">.models</span> <span class="k">import</span> <span class="n">Question</span>


<span class="k">def</span> <span class="nf">index</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
    <span class="n">latest_question_list</span> <span class="o">=</span> <span class="n">Question</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="s1">&#39;-pub_date&#39;</span><span class="p">)[:</span><span class="mi">5</span><span class="p">]</span>
    <span class="n">template</span> <span class="o">=</span> <span class="n">loader</span><span class="o">.</span><span class="n">get_template</span><span class="p">(</span><span class="s1">&#39;polls/index.html&#39;</span><span class="p">)</span>
    <span class="n">context</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">&#39;latest_question_list&#39;</span><span class="p">:</span> <span class="n">latest_question_list</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="n">template</span><span class="o">.</span><span class="n">render</span><span class="p">(</span><span class="n">context</span><span class="p">,</span> <span class="n">request</span><span class="p">))</span>
</pre></div>
</div>
<p>That code loads the template called  <code class="docutils literal"><span class="pre">polls/index.html</span></code> and passes it a
context. The context is a dictionary mapping template variable names to Python
objects.</p>
<p>Load the page by pointing your browser at &#8220;/polls/&#8221;, and you should see a
bulleted-list containing the &#8220;What&#8217;s up&#8221; question from <a class="reference internal" href="../tutorial02/"><span class="doc">Tutorial 2</span></a>. The link points to the question&#8217;s detail page.</p>
<div class="section" id="s-a-shortcut-render">
<span id="a-shortcut-render"></span><h3>A shortcut: <a class="reference internal" href="../../topics/http/shortcuts/#django.shortcuts.render" title="django.shortcuts.render"><code class="xref py py-func docutils literal"><span class="pre">render()</span></code></a><a class="headerlink" href="#a-shortcut-render" title="Permalink to this headline">¶</a></h3>
<p>It&#8217;s a very common idiom to load a template, fill a context and return an
<a class="reference internal" href="../../ref/request-response/#django.http.HttpResponse" title="django.http.HttpResponse"><code class="xref py py-class docutils literal"><span class="pre">HttpResponse</span></code></a> object with the result of the rendered
template. Django provides a shortcut. Here&#8217;s the full <code class="docutils literal"><span class="pre">index()</span></code> view,
rewritten:</p>
<div class="highlight-default snippet"><div class="snippet-filename">polls/views.py</div>
<div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">django.shortcuts</span> <span class="k">import</span> <span class="n">render</span>

<span class="kn">from</span> <span class="nn">.models</span> <span class="k">import</span> <span class="n">Question</span>


<span class="k">def</span> <span class="nf">index</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
    <span class="n">latest_question_list</span> <span class="o">=</span> <span class="n">Question</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="s1">&#39;-pub_date&#39;</span><span class="p">)[:</span><span class="mi">5</span><span class="p">]</span>
    <span class="n">context</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;latest_question_list&#39;</span><span class="p">:</span> <span class="n">latest_question_list</span><span class="p">}</span>
    <span class="k">return</span> <span class="n">render</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="s1">&#39;polls/index.html&#39;</span><span class="p">,</span> <span class="n">context</span><span class="p">)</span>
</pre></div>
</div>
<p>Note that once we&#8217;ve done this in all these views, we no longer need to import
<a class="reference internal" href="../../topics/templates/#module-django.template.loader" title="django.template.loader"><code class="xref py py-mod docutils literal"><span class="pre">loader</span></code></a> and <a class="reference internal" href="../../ref/request-response/#django.http.HttpResponse" title="django.http.HttpResponse"><code class="xref py py-class docutils literal"><span class="pre">HttpResponse</span></code></a> (you&#8217;ll
want to keep <code class="docutils literal"><span class="pre">HttpResponse</span></code> if you still have the stub methods for <code class="docutils literal"><span class="pre">detail</span></code>,
<code class="docutils literal"><span class="pre">results</span></code>, and <code class="docutils literal"><span class="pre">vote</span></code>).</p>
<p>The <a class="reference internal" href="../../topics/http/shortcuts/#django.shortcuts.render" title="django.shortcuts.render"><code class="xref py py-func docutils literal"><span class="pre">render()</span></code></a> function takes the request object as its
first argument, a template name as its second argument and a dictionary as its
optional third argument. It returns an <a class="reference internal" href="../../ref/request-response/#django.http.HttpResponse" title="django.http.HttpResponse"><code class="xref py py-class docutils literal"><span class="pre">HttpResponse</span></code></a>
object of the given template rendered with the given context.</p>
</div>
</div>
<div class="section" id="s-raising-a-404-error">
<span id="raising-a-404-error"></span><h2>Raising a 404 error<a class="headerlink" href="#raising-a-404-error" title="Permalink to this headline">¶</a></h2>
<p>Now, let&#8217;s tackle the question detail view &#8211; the page that displays the question text
for a given poll. Here&#8217;s the view:</p>
<div class="highlight-default snippet"><div class="snippet-filename">polls/views.py</div>
<div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">django.http</span> <span class="k">import</span> <span class="n">Http404</span>
<span class="kn">from</span> <span class="nn">django.shortcuts</span> <span class="k">import</span> <span class="n">render</span>

<span class="kn">from</span> <span class="nn">.models</span> <span class="k">import</span> <span class="n">Question</span>
<span class="c1"># ...</span>
<span class="k">def</span> <span class="nf">detail</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">question_id</span><span class="p">):</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">question</span> <span class="o">=</span> <span class="n">Question</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">pk</span><span class="o">=</span><span class="n">question_id</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">Question</span><span class="o">.</span><span class="n">DoesNotExist</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">Http404</span><span class="p">(</span><span class="s2">&quot;Question does not exist&quot;</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">render</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="s1">&#39;polls/detail.html&#39;</span><span class="p">,</span> <span class="p">{</span><span class="s1">&#39;question&#39;</span><span class="p">:</span> <span class="n">question</span><span class="p">})</span>
</pre></div>
</div>
<p>The new concept here: The view raises the <a class="reference internal" href="../../topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a> exception
if a question with the requested ID doesn&#8217;t exist.</p>
<p>We&#8217;ll discuss what you could put in that <code class="docutils literal"><span class="pre">polls/detail.html</span></code> template a bit
later, but if you&#8217;d like to quickly get the above example working, a file
containing just:</p>
<div class="highlight-html+django snippet"><div class="snippet-filename">polls/templates/polls/detail.html</div>
<div class="highlight"><pre><span></span><span class="cp">{{</span> <span class="nv">question</span> <span class="cp">}}</span>
</pre></div>
</div>
<p>will get you started for now.</p>
<div class="section" id="s-a-shortcut-get-object-or-404">
<span id="a-shortcut-get-object-or-404"></span><h3>A shortcut: <a class="reference internal" href="../../topics/http/shortcuts/#django.shortcuts.get_object_or_404" title="django.shortcuts.get_object_or_404"><code class="xref py py-func docutils literal"><span class="pre">get_object_or_404()</span></code></a><a class="headerlink" href="#a-shortcut-get-object-or-404" title="Permalink to this headline">¶</a></h3>
<p>It&#8217;s a very common idiom to use <a class="reference internal" href="../../ref/models/querysets/#django.db.models.query.QuerySet.get" title="django.db.models.query.QuerySet.get"><code class="xref py py-meth docutils literal"><span class="pre">get()</span></code></a>
and raise <a class="reference internal" href="../../topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a> if the object doesn&#8217;t exist. Django
provides a shortcut. Here&#8217;s the <code class="docutils literal"><span class="pre">detail()</span></code> view, rewritten:</p>
<div class="highlight-default snippet"><div class="snippet-filename">polls/views.py</div>
<div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">django.shortcuts</span> <span class="k">import</span> <span class="n">get_object_or_404</span><span class="p">,</span> <span class="n">render</span>

<span class="kn">from</span> <span class="nn">.models</span> <span class="k">import</span> <span class="n">Question</span>
<span class="c1"># ...</span>
<span class="k">def</span> <span class="nf">detail</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">question_id</span><span class="p">):</span>
    <span class="n">question</span> <span class="o">=</span> <span class="n">get_object_or_404</span><span class="p">(</span><span class="n">Question</span><span class="p">,</span> <span class="n">pk</span><span class="o">=</span><span class="n">question_id</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">render</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="s1">&#39;polls/detail.html&#39;</span><span class="p">,</span> <span class="p">{</span><span class="s1">&#39;question&#39;</span><span class="p">:</span> <span class="n">question</span><span class="p">})</span>
</pre></div>
</div>
<p>The <a class="reference internal" href="../../topics/http/shortcuts/#django.shortcuts.get_object_or_404" title="django.shortcuts.get_object_or_404"><code class="xref py py-func docutils literal"><span class="pre">get_object_or_404()</span></code></a> function takes a Django model
as its first argument and an arbitrary number of keyword arguments, which it
passes to the <a class="reference internal" href="../../ref/models/querysets/#django.db.models.query.QuerySet.get" title="django.db.models.query.QuerySet.get"><code class="xref py py-meth docutils literal"><span class="pre">get()</span></code></a> function of the
model&#8217;s manager. It raises <a class="reference internal" href="../../topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a> if the object doesn&#8217;t
exist.</p>
<div class="admonition-philosophy admonition">
<p class="first admonition-title">Philosophy</p>
<p>Why do we use a helper function <a class="reference internal" href="../../topics/http/shortcuts/#django.shortcuts.get_object_or_404" title="django.shortcuts.get_object_or_404"><code class="xref py py-func docutils literal"><span class="pre">get_object_or_404()</span></code></a>
instead of automatically catching the
<a class="reference internal" href="../../ref/exceptions/#django.core.exceptions.ObjectDoesNotExist" title="django.core.exceptions.ObjectDoesNotExist"><code class="xref py py-exc docutils literal"><span class="pre">ObjectDoesNotExist</span></code></a> exceptions at a higher
level, or having the model API raise <a class="reference internal" href="../../topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a> instead of
<a class="reference internal" href="../../ref/exceptions/#django.core.exceptions.ObjectDoesNotExist" title="django.core.exceptions.ObjectDoesNotExist"><code class="xref py py-exc docutils literal"><span class="pre">ObjectDoesNotExist</span></code></a>?</p>
<p class="last">Because that would couple the model layer to the view layer. One of the
foremost design goals of Django is to maintain loose coupling. Some
controlled coupling is introduced in the <a class="reference internal" href="../../topics/http/shortcuts/#module-django.shortcuts" title="django.shortcuts: Convenience shortcuts that span multiple levels of Django's MVC stack."><code class="xref py py-mod docutils literal"><span class="pre">django.shortcuts</span></code></a> module.</p>
</div>
<p>There&#8217;s also a <a class="reference internal" href="../../topics/http/shortcuts/#django.shortcuts.get_list_or_404" title="django.shortcuts.get_list_or_404"><code class="xref py py-func docutils literal"><span class="pre">get_list_or_404()</span></code></a> function, which works
just as <a class="reference internal" href="../../topics/http/shortcuts/#django.shortcuts.get_object_or_404" title="django.shortcuts.get_object_or_404"><code class="xref py py-func docutils literal"><span class="pre">get_object_or_404()</span></code></a> &#8211; except using
<a class="reference internal" href="../../ref/models/querysets/#django.db.models.query.QuerySet.filter" title="django.db.models.query.QuerySet.filter"><code class="xref py py-meth docutils literal"><span class="pre">filter()</span></code></a> instead of
<a class="reference internal" href="../../ref/models/querysets/#django.db.models.query.QuerySet.get" title="django.db.models.query.QuerySet.get"><code class="xref py py-meth docutils literal"><span class="pre">get()</span></code></a>. It raises
<a class="reference internal" href="../../topics/http/views/#django.http.Http404" title="django.http.Http404"><code class="xref py py-exc docutils literal"><span class="pre">Http404</span></code></a> if the list is empty.</p>
</div>
</div>
<div class="section" id="s-use-the-template-system">
<span id="use-the-template-system"></span><h2>Use the template system<a class="headerlink" href="#use-the-template-system" title="Permalink to this headline">¶</a></h2>
<p>Back to the <code class="docutils literal"><span class="pre">detail()</span></code> view for our poll application. Given the context
variable <code class="docutils literal"><span class="pre">question</span></code>, here&#8217;s what the <code class="docutils literal"><span class="pre">polls/detail.html</span></code> template might look
like:</p>
<div class="highlight-html+django snippet"><div class="snippet-filename">polls/templates/polls/detail.html</div>
<div class="highlight"><pre><span></span><span class="p">&lt;</span><span class="nt">h1</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">h1</span><span class="p">&gt;</span>
<span class="p">&lt;</span><span class="nt">ul</span><span class="p">&gt;</span>
<span class="cp">{%</span> <span class="k">for</span> <span class="nv">choice</span> <span class="k">in</span> <span class="nv">question.choice_set.all</span> <span class="cp">%}</span>
    <span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">choice.choice_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
<span class="cp">{%</span> <span class="k">endfor</span> <span class="cp">%}</span>
<span class="p">&lt;/</span><span class="nt">ul</span><span class="p">&gt;</span>
</pre></div>
</div>
<p>The template system uses dot-lookup syntax to access variable attributes. In
the example of <code class="docutils literal"><span class="pre">{{</span> <span class="pre">question.question_text</span> <span class="pre">}}</span></code>, first Django does a dictionary lookup
on the object <code class="docutils literal"><span class="pre">question</span></code>. Failing that, it tries an attribute lookup &#8211; which
works, in this case. If attribute lookup had failed, it would&#8217;ve tried a
list-index lookup.</p>
<p>Method-calling happens in the <a class="reference internal" href="../../ref/templates/builtins/#std:templatetag-for"><code class="xref std std-ttag docutils literal"><span class="pre">{%</span> <span class="pre">for</span> <span class="pre">%}</span></code></a> loop:
<code class="docutils literal"><span class="pre">question.choice_set.all</span></code> is interpreted as the Python code
<code class="docutils literal"><span class="pre">question.choice_set.all()</span></code>, which returns an iterable of <code class="docutils literal"><span class="pre">Choice</span></code> objects and is
suitable for use in the <a class="reference internal" href="../../ref/templates/builtins/#std:templatetag-for"><code class="xref std std-ttag docutils literal"><span class="pre">{%</span> <span class="pre">for</span> <span class="pre">%}</span></code></a> tag.</p>
<p>See the <a class="reference internal" href="../../topics/templates/"><span class="doc">template guide</span></a> for more about templates.</p>
</div>
<div class="section" id="s-removing-hardcoded-urls-in-templates">
<span id="removing-hardcoded-urls-in-templates"></span><h2>Removing hardcoded URLs in templates<a class="headerlink" href="#removing-hardcoded-urls-in-templates" title="Permalink to this headline">¶</a></h2>
<p>Remember, when we wrote the link to a question in the <code class="docutils literal"><span class="pre">polls/index.html</span></code>
template, the link was partially hardcoded like this:</p>
<div class="highlight-html+django"><div class="highlight"><pre><span></span><span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;/polls/</span><span class="cp">{{</span> <span class="nv">question.id</span> <span class="cp">}}</span><span class="s">/&quot;</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
</pre></div>
</div>
<p>The problem with this hardcoded, tightly-coupled approach is that it becomes
challenging to change URLs on projects with a lot of templates. However, since
you defined the name argument in the <a class="reference internal" href="../../ref/urls/#django.conf.urls.url" title="django.conf.urls.url"><code class="xref py py-func docutils literal"><span class="pre">url()</span></code></a> functions in
the <code class="docutils literal"><span class="pre">polls.urls</span></code> module, you can remove a reliance on specific URL paths
defined in your url configurations by using the <code class="docutils literal"><span class="pre">{%</span> <span class="pre">url</span> <span class="pre">%}</span></code> template tag:</p>
<div class="highlight-html+django"><div class="highlight"><pre><span></span><span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;</span><span class="cp">{%</span> <span class="k">url</span> <span class="s1">&#39;detail&#39;</span> <span class="nv">question.id</span> <span class="cp">%}</span><span class="s">&quot;</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
</pre></div>
</div>
<p>The way this works is by looking up the URL definition as specified in the
<code class="docutils literal"><span class="pre">polls.urls</span></code> module. You can see exactly where the URL name of &#8216;detail&#8217; is
defined below:</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="o">...</span>
<span class="c1"># the &#39;name&#39; value as called by the {% url %} template tag</span>
<span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^(?P&lt;question_id&gt;[0-9]+)/$&#39;</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">detail</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;detail&#39;</span><span class="p">),</span>
<span class="o">...</span>
</pre></div>
</div>
<p>If you want to change the URL of the polls detail view to something else,
perhaps to something like <code class="docutils literal"><span class="pre">polls/specifics/12/</span></code> instead of doing it in the
template (or templates) you would change it in <code class="docutils literal"><span class="pre">polls/urls.py</span></code>:</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="o">...</span>
<span class="c1"># added the word &#39;specifics&#39;</span>
<span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^specifics/(?P&lt;question_id&gt;[0-9]+)/$&#39;</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">detail</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;detail&#39;</span><span class="p">),</span>
<span class="o">...</span>
</pre></div>
</div>
</div>
<div class="section" id="s-namespacing-url-names">
<span id="namespacing-url-names"></span><h2>Namespacing URL names<a class="headerlink" href="#namespacing-url-names" title="Permalink to this headline">¶</a></h2>
<p>The tutorial project has just one app, <code class="docutils literal"><span class="pre">polls</span></code>. In real Django projects,
there might be five, ten, twenty apps or more. How does Django differentiate
the URL names between them? For example, the <code class="docutils literal"><span class="pre">polls</span></code> app has a <code class="docutils literal"><span class="pre">detail</span></code>
view, and so might an app on the same project that is for a blog. How does one
make it so that Django knows which app view to create for a url when using the
<code class="docutils literal"><span class="pre">{%</span> <span class="pre">url</span> <span class="pre">%}</span></code> template tag?</p>
<p>The answer is to add namespaces to your  URLconf. In the <code class="docutils literal"><span class="pre">polls/urls.py</span></code>
file, go ahead and add an <code class="docutils literal"><span class="pre">app_name</span></code> to set the application namespace:</p>
<div class="highlight-default snippet"><div class="snippet-filename">polls/urls.py</div>
<div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">django.conf.urls</span> <span class="k">import</span> <span class="n">url</span>

<span class="kn">from</span> <span class="nn">.</span> <span class="k">import</span> <span class="n">views</span>

<span class="n">app_name</span> <span class="o">=</span> <span class="s1">&#39;polls&#39;</span>
<span class="n">urlpatterns</span> <span class="o">=</span> <span class="p">[</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^$&#39;</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">index</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;index&#39;</span><span class="p">),</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^(?P&lt;question_id&gt;[0-9]+)/$&#39;</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">detail</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;detail&#39;</span><span class="p">),</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^(?P&lt;question_id&gt;[0-9]+)/results/$&#39;</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">results</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;results&#39;</span><span class="p">),</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^(?P&lt;question_id&gt;[0-9]+)/vote/$&#39;</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">vote</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;vote&#39;</span><span class="p">),</span>
<span class="p">]</span>
</pre></div>
</div>
<p>Now change your <code class="docutils literal"><span class="pre">polls/index.html</span></code> template from:</p>
<div class="highlight-html+django snippet"><div class="snippet-filename">polls/templates/polls/index.html</div>
<div class="highlight"><pre><span></span><span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;</span><span class="cp">{%</span> <span class="k">url</span> <span class="s1">&#39;detail&#39;</span> <span class="nv">question.id</span> <span class="cp">%}</span><span class="s">&quot;</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
</pre></div>
</div>
<p>to point at the namespaced detail view:</p>
<div class="highlight-html+django snippet"><div class="snippet-filename">polls/templates/polls/index.html</div>
<div class="highlight"><pre><span></span><span class="p">&lt;</span><span class="nt">li</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;</span><span class="cp">{%</span> <span class="k">url</span> <span class="s1">&#39;polls:detail&#39;</span> <span class="nv">question.id</span> <span class="cp">%}</span><span class="s">&quot;</span><span class="p">&gt;</span><span class="cp">{{</span> <span class="nv">question.question_text</span> <span class="cp">}}</span><span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">li</span><span class="p">&gt;</span>
</pre></div>
</div>
<p>When you&#8217;re comfortable with writing views, read <a class="reference internal" href="../tutorial04/"><span class="doc">part 4 of this tutorial</span></a> to learn about simple form processing and generic views.</p>
</div>
</div>

</div>



<div class="browse-horizontal">
  
  <div class="left"><a href="../tutorial02/"><i class="icon icon-chevron-left"></i> Writing your first Django app, part 2</a></div>
  
  
  <div class="right"><a href="../tutorial04/">Writing your first Django app, part 4 <i class="icon icon-chevron-right"></i></a></div>
  
</div>



        <a href="#top" class="backtotop"><i class="icon icon-chevron-up"></i> Back to Top</a>
      </div>

      
<h1 class="visuallyhidden">Additional Information</h1>
<div role="complementary">
  
  

<form action="https://docs.djangoproject.com/en/1.11/search/" class="search form-input" role="search">
  <label class="visuallyhidden" for="news-search">Search:</label>
    <input id="id_q" name="q" placeholder="Search 1.11 documentation" type="search" />

    <button type="submit">
      <i class="icon icon-search"></i>
      <span class="visuallyhidden">Search</span>
    </button>
</form>

  

  


  <div class="fundraising-sidebar">
    <h2>Support Django!</h2>

    <div class="small-heart">
      <img src="/s/img/small-fundraising-heart.d255f6e934e5.png" alt="Support Django!" />
    </div>

    <div class="small-cta">
      <ul class="list-links-small">
        <li><a href="https://www.djangoproject.com/fundraising/">
          MashTime.com donated to the Django Software Foundation to
          support Django development. Donate today!
        </a></li>
      </ul>
    </div>
  </div>



  
    <h2>Contents</h2>
    
    <ul>
<li><a class="reference internal" href="#">Writing your first Django app, part 3</a><ul>
<li><a class="reference internal" href="#overview">Overview</a></li>
<li><a class="reference internal" href="#writing-more-views">Writing more views</a></li>
<li><a class="reference internal" href="#write-views-that-actually-do-something">Write views that actually do something</a><ul>
<li><a class="reference internal" href="#a-shortcut-render">A shortcut: <code class="docutils literal"><span class="pre">render()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#raising-a-404-error">Raising a 404 error</a><ul>
<li><a class="reference internal" href="#a-shortcut-get-object-or-404">A shortcut: <code class="docutils literal"><span class="pre">get_object_or_404()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#use-the-template-system">Use the template system</a></li>
<li><a class="reference internal" href="#removing-hardcoded-urls-in-templates">Removing hardcoded URLs in templates</a></li>
<li><a class="reference internal" href="#namespacing-url-names">Namespacing URL names</a></li>
</ul>
</li>
</ul>

    
  

  
  <h2>Browse</h2>
  <ul>
    
    
    <li>Prev: <a href="../tutorial02/">Writing your first Django app, part 2</a></li>
    
    
    <li>Next: <a href="../tutorial04/">Writing your first Django app, part 4</a></li>
    
    <li><a href="https://docs.djangoproject.com/en/1.11/contents/">Table of contents</a></li>
    
    <li><a href="https://docs.djangoproject.com/en/1.11/genindex/">General Index</a></li>
    
    <li><a href="https://docs.djangoproject.com/en/1.11/py-modindex/">Python Module Index</a></li>
    
    
  </ul>
  

  
  <h2>You are here:</h2>
  <ul>
    <li>
      <a href="https://docs.djangoproject.com/en/1.11/">Django 1.11 documentation</a>
      
      <ul><li><a href="../">Getting started</a>
      
      <ul><li>Writing your first Django app, part 3</li></ul>
      </li></ul>
    </li>
  </ul>
  

  
  <h2 id="getting-help-sidebar">Getting help</h2>
  <dl class="list-links">
    <dt><a href="https://docs.djangoproject.com/en/1.11/faq/">FAQ</a></dt>
    <dd>Try the FAQ — it's got answers to many common questions.</dd>

    <dt><a href="/en/stable/genindex/">Index</a>, <a href="/en/stable/py-modindex/">Module Index</a>, or <a href="/en/stable/contents/">Table of Contents</a></dt>
    <dd>Handy when looking for specific information.</dd>

    <dt><a href="http://groups.google.com/group/django-users/">django-users mailing list</a></dt>
    <dd>Search for information in the archives of the django-users mailing list, or post a question.</dd>

    <dt><a href="irc://irc.freenode.net/django">#django IRC channel</a></dt>
    <dd>Ask a question in the #django IRC channel, or search the IRC logs to see if it’s been asked before.</dd>

    <dt><a href="http://code.djangoproject.com/">Ticket tracker</a></dt>
    <dd>Report bugs with Django or Django documentation in our ticket tracker.</dd>
  </dl>
  

  
  <h2>Download:</h2>
  <p>
    Offline (Django 1.11):
    <a href="/m/docs/django-docs-1.11-en.zip">HTML</a> |
    <a href="https://media.readthedocs.org/pdf/django/1.11.x/django.pdf">PDF</a> |
    <a href="https://media.readthedocs.org/epub/django/1.11.x/django.epub">ePub</a>
    <br>
    <span class="quiet">
      Provided by <a href="https://readthedocs.org/">Read the Docs</a>.
    </span>
  </p>
  
</div>

      

    </div>

     
     

    
    
    

    
      
<div role="contentinfo">
  <div class="subfooter">
    <div class="container">
      <h1 class="visuallyhidden">Django Links</h1>

      <div class="col learn">
        <h2>Learn More</h2>
        <ul>
          <li><a href="https://www.djangoproject.com/start/overview/">About Django</a></li>
          
          <li><a href="https://www.djangoproject.com/start/">Getting Started with Django</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/organization/">Team Organization</a></li>
          <li><a href="https://www.djangoproject.com/foundation/">Django Software Foundation</a></li>
          <li><a href="https://www.djangoproject.com/conduct/">Code of Conduct</a></li>
          <li><a href="https://www.djangoproject.com/diversity/">Diversity Statement</a></li>
        </ul>
      </div>

      <div class="col involved">
        <h2>Get Involved</h2>
        <ul>
          <li><a href="https://www.djangoproject.com/community/">Join a Group</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/contributing/">Contribute to Django</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/">Submit a Bug</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues">Report a Security Issue</a></li>
        </ul>
      </div>

      <div class="col follow last-child">
        <h2>Follow Us</h2>
        <ul>
          <li><a href="https://github.com/django">GitHub</a></li>
          <li><a href="https://twitter.com/djangoproject">Twitter</a></li>
          <li><a href="https://www.djangoproject.com/rss/weblog/">News RSS</a></li>
          <li><a href="https://groups.google.com/forum/#!forum/django-users">Django Users Mailing List</a></li>
        </ul>
      </div>

    </div>
  </div>

  <div class="footer">
    <div class="container">
      <div class="footer-logo">
        <a class="logo" href="https://www.djangoproject.com/">Django</a>
      </div>
      <ul class="thanks">
        <li>
          <span>Hosting by</span> <a class="rackspace" href="http://rackspace.com">Rackspace</a>
          <span>Search by</span> <a class="elastic" href="https://www.elastic.co">Elastic Search</a>
        </li>
        <li class="design"><span>Design by</span> <a class="threespot" href="http://www.threespot.com">Threespot</a> <span class="ampersand">&amp;</span> <a class="andrevv" href="http://andrevv.com/"></a></li>
      </ul>
      <p class="copyright">&copy; 2005-2017
        <a href="https://www.djangoproject.com/foundation/"> Django Software
        Foundation</a> and individual contributors. Django is a
        <a href="https://www.djangoproject.com/trademarks/">registered
        trademark</a> of the Django Software Foundation.
      </p>
    </div>
  </div>

</div>

    

    
    <script>
    function extless(input) {
        return input.replace(/(.*)\.[^.]+$/, '$1');
    }
    var require = {
        shim: {
            'jquery': [],
            'jquery.inview': ["jquery"],
            'jquery.payment': ["jquery"],
            'jquery.flot': ["jquery"],
            'jquery.unveil': ["jquery"],
            'stripe': {
              exports: 'Stripe'
            }
        },
        paths: {
            "jquery": extless("/s/js/lib/jquery/dist/jquery.min.87e69028f78d.js"),
            "jquery.inview": extless("/s/js/lib/jquery.inview/jquery.inview.min.4edba1c65592.js"),
            "jquery.payment": extless("/s/js/lib/jquery.payment/lib/jquery.payment.e99c05ca79ae.js"),
            "jquery.unveil": extless("/s/js/lib/unveil/jquery.unveil.min.ac79eb277093.js"),
            "jquery.flot": extless("/s/js/lib/jquery-flot/jquery.flot.min.9964206e9d7f.js"),
            "clipboard": extless("/s/js/lib/clipboard/dist/clipboard.min.bd70fd596a23.js"),
            "mod/floating-warning": extless("/s/js/mod/floating-warning.a21b2abd2884.js"),
            "mod/list-collapsing": extless("/s/js/mod/list-collapsing.c1a08d3ef9e9.js"),
            "mod/list-feature": extless("/s/js/mod/list-feature.73529480f25b.js"),
            "mod/mobile-menu": extless("/s/js/mod/mobile-menu.841726ee903a.js"),
            "mod/version-switcher": extless("/s/js/mod/version-switcher.c28bb83972bb.js"),
            "mod/search-key": extless("/s/js/mod/search-key.f3c0a6fcfedd.js"),
            "mod/stripe-custom-checkout": extless("/s/js/mod/stripe-custom-checkout.e299868f75aa.js"),
            "mod/stripe-change-card": extless("/s/js/mod/stripe-change-card.c9e3d05f7a91.js"),
            "stripe-checkout": "https://checkout.stripe.com/checkout",
            "stripe": "https://js.stripe.com/v2/?"  // ? needed due to require.js
        }
    };
    </script>
    <script data-main="/s/js/main.3a2ae4b1529c.js" src="/s/js/lib/require.177879fbe7dd.js"></script>
    



  </body>
</html>
