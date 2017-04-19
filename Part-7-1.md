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

    <title>Advanced tutorial: How to write reusable apps | Django documentation | Django</title>

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
    
  
    
      
    
  
  <link rel="canonical" href="https://docs.djangoproject.com/en/1.11/intro/reusable-apps/">
  
    
        
          
        
        
        <link rel="alternate"
           hreflang="el"
           href="https://docs.djangoproject.com/el/1.11/intro/reusable-apps/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="x-default"
           href="https://docs.djangoproject.com/en/1.11/intro/reusable-apps/">
        
        <link rel="alternate"
           hreflang="en"
           href="https://docs.djangoproject.com/en/1.11/intro/reusable-apps/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="es"
           href="https://docs.djangoproject.com/es/1.11/intro/reusable-apps/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="fr"
           href="https://docs.djangoproject.com/fr/1.11/intro/reusable-apps/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="id"
           href="https://docs.djangoproject.com/id/1.11/intro/reusable-apps/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="ja"
           href="https://docs.djangoproject.com/ja/1.11/intro/reusable-apps/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="pl"
           href="https://docs.djangoproject.com/pl/1.11/intro/reusable-apps/">
    
        
          
        
        
        <link rel="alternate"
           hreflang="pt-br"
           href="https://docs.djangoproject.com/pt-br/1.11/intro/reusable-apps/">
    
  

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
    
      
    
    <a href="https://docs.djangoproject.com/el/1.11/intro/reusable-apps/">el</a>
  </li>
  
  
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/es/1.11/intro/reusable-apps/">es</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/fr/1.11/intro/reusable-apps/">fr</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/id/1.11/intro/reusable-apps/">id</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/ja/1.11/intro/reusable-apps/">ja</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/pl/1.11/intro/reusable-apps/">pl</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/pt-br/1.11/intro/reusable-apps/">pt-br</a>
  </li>
  
  
    <li class="current"
        title="Click on the links on the left to switch to another language.">
      <span>Language: <strong>en</strong></span>
    </li>
  </ul>

  
  <ul id="doc-versions" class="version-switcher">
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.7/intro/reusable-apps/">1.7</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.8/intro/reusable-apps/">1.8</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.9/intro/reusable-apps/">1.9</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.10/intro/reusable-apps/">1.10</a>
    </li>
    
    
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/dev/intro/reusable-apps/">dev</a>
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
<div class="section" id="s-advanced-tutorial-how-to-write-reusable-apps">
<span id="advanced-tutorial-how-to-write-reusable-apps"></span><h1>Advanced tutorial: How to write reusable apps<a class="headerlink" href="#advanced-tutorial-how-to-write-reusable-apps" title="Permalink to this headline">¶</a></h1>
<p>This advanced tutorial begins where <a class="reference internal" href="../tutorial07/"><span class="doc">Tutorial 7</span></a>
left off. We&#8217;ll be turning our Web-poll into a standalone Python package
you can reuse in new projects and share with other people.</p>
<p>If you haven&#8217;t recently completed Tutorials 1–7, we encourage you to review
these so that your example project matches the one described below.</p>
<div class="section" id="s-reusability-matters">
<span id="reusability-matters"></span><h2>Reusability matters<a class="headerlink" href="#reusability-matters" title="Permalink to this headline">¶</a></h2>
<p>It&#8217;s a lot of work to design, build, test and maintain a web application. Many
Python and Django projects share common problems. Wouldn&#8217;t it be great if we
could save some of this repeated work?</p>
<p>Reusability is the way of life in Python. <a class="reference external" href="https://pypi.python.org/pypi">The Python Package Index (PyPI)</a> has a vast range of packages you can use in
your own Python programs. Check out <a class="reference external" href="https://www.djangopackages.com">Django Packages</a> for existing reusable apps you could
incorporate in your project. Django itself is also just a Python package. This
means that you can take existing Python packages or Django apps and compose
them into your own web project. You only need to write the parts that make
your project unique.</p>
<p>Let&#8217;s say you were starting a new project that needed a polls app like the one
we&#8217;ve been working on. How do you make this app reusable? Luckily, you&#8217;re well
on the way already. In <a class="reference internal" href="../tutorial03/"><span class="doc">Tutorial 3</span></a>, we saw how we
could decouple polls from the project-level URLconf using an <code class="docutils literal"><span class="pre">include</span></code>.
In this tutorial, we&#8217;ll take further steps to make the app easy to use in new
projects and ready to publish for others to install and use.</p>
<div class="admonition-package-app admonition">
<p class="first admonition-title">Package? App?</p>
<p>A Python <a class="reference external" href="https://docs.python.org/3/glossary.html#term-package" title="(in Python v3.6)"><span class="xref std std-term">package</span></a> provides a way of grouping related Python code for
easy reuse. A package contains one or more files of Python code (also known
as &#8220;modules&#8221;).</p>
<p>A package can be imported with <code class="docutils literal"><span class="pre">import</span> <span class="pre">foo.bar</span></code> or <code class="docutils literal"><span class="pre">from</span> <span class="pre">foo</span> <span class="pre">import</span>
<span class="pre">bar</span></code>. For a directory (like <code class="docutils literal"><span class="pre">polls</span></code>) to form a package, it must contain
a special file <code class="docutils literal"><span class="pre">__init__.py</span></code>, even if this file is empty.</p>
<p>A Django <em>application</em> is just a Python package that is specifically
intended for use in a Django project. An application may use common Django
conventions, such as having <code class="docutils literal"><span class="pre">models</span></code>, <code class="docutils literal"><span class="pre">tests</span></code>, <code class="docutils literal"><span class="pre">urls</span></code>, and <code class="docutils literal"><span class="pre">views</span></code>
submodules.</p>
<p class="last">Later on we use the term <em>packaging</em> to describe the process of making a
Python package easy for others to install. It can be a little confusing, we
know.</p>
</div>
</div>
<div class="section" id="s-your-project-and-your-reusable-app">
<span id="your-project-and-your-reusable-app"></span><h2>Your project and your reusable app<a class="headerlink" href="#your-project-and-your-reusable-app" title="Permalink to this headline">¶</a></h2>
<p>After the previous tutorials, our project should look like this:</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="n">mysite</span><span class="o">/</span>
    <span class="n">manage</span><span class="o">.</span><span class="n">py</span>
    <span class="n">mysite</span><span class="o">/</span>
        <span class="fm">__init__</span><span class="o">.</span><span class="n">py</span>
        <span class="n">settings</span><span class="o">.</span><span class="n">py</span>
        <span class="n">urls</span><span class="o">.</span><span class="n">py</span>
        <span class="n">wsgi</span><span class="o">.</span><span class="n">py</span>
    <span class="n">polls</span><span class="o">/</span>
        <span class="fm">__init__</span><span class="o">.</span><span class="n">py</span>
        <span class="n">admin</span><span class="o">.</span><span class="n">py</span>
        <span class="n">migrations</span><span class="o">/</span>
            <span class="fm">__init__</span><span class="o">.</span><span class="n">py</span>
            <span class="mi">0001</span><span class="n">_initial</span><span class="o">.</span><span class="n">py</span>
        <span class="n">models</span><span class="o">.</span><span class="n">py</span>
        <span class="n">static</span><span class="o">/</span>
            <span class="n">polls</span><span class="o">/</span>
                <span class="n">images</span><span class="o">/</span>
                    <span class="n">background</span><span class="o">.</span><span class="n">gif</span>
                <span class="n">style</span><span class="o">.</span><span class="n">css</span>
        <span class="n">templates</span><span class="o">/</span>
            <span class="n">polls</span><span class="o">/</span>
                <span class="n">detail</span><span class="o">.</span><span class="n">html</span>
                <span class="n">index</span><span class="o">.</span><span class="n">html</span>
                <span class="n">results</span><span class="o">.</span><span class="n">html</span>
        <span class="n">tests</span><span class="o">.</span><span class="n">py</span>
        <span class="n">urls</span><span class="o">.</span><span class="n">py</span>
        <span class="n">views</span><span class="o">.</span><span class="n">py</span>
    <span class="n">templates</span><span class="o">/</span>
        <span class="n">admin</span><span class="o">/</span>
            <span class="n">base_site</span><span class="o">.</span><span class="n">html</span>
</pre></div>
</div>
<p>You created <code class="docutils literal"><span class="pre">mysite/templates</span></code> in <a class="reference internal" href="../tutorial07/"><span class="doc">Tutorial 7</span></a>,
and <code class="docutils literal"><span class="pre">polls/templates</span></code> in <a class="reference internal" href="../tutorial03/"><span class="doc">Tutorial 3</span></a>. Now perhaps
it is clearer why we chose to have separate template directories for the
project and application: everything that is part of the polls application is in
<code class="docutils literal"><span class="pre">polls</span></code>. It makes the application self-contained and easier to drop into a
new project.</p>
<p>The <code class="docutils literal"><span class="pre">polls</span></code> directory could now be copied into a new Django project and
immediately reused. It&#8217;s not quite ready to be published though. For that, we
need to package the app to make it easy for others to install.</p>
</div>
<div class="section" id="s-installing-some-prerequisites">
<span id="s-installing-reusable-apps-prerequisites"></span><span id="installing-some-prerequisites"></span><span id="installing-reusable-apps-prerequisites"></span><h2>Installing some prerequisites<a class="headerlink" href="#installing-some-prerequisites" title="Permalink to this headline">¶</a></h2>
<p>The current state of Python packaging is a bit muddled with various tools. For
this tutorial, we&#8217;re going to use <a class="reference external" href="https://pypi.python.org/pypi/setuptools">setuptools</a> to build our package. It&#8217;s the
recommended packaging tool (merged with the <code class="docutils literal"><span class="pre">distribute</span></code> fork). We&#8217;ll also be
using <a class="reference external" href="https://pypi.python.org/pypi/pip">pip</a> to install and uninstall it. You should install these
two packages now. If you need help, you can refer to <a class="reference internal" href="../../topics/install/#installing-official-release"><span class="std std-ref">how to install
Django with pip</span></a>. You can install <code class="docutils literal"><span class="pre">setuptools</span></code>
the same way.</p>
</div>
<div class="section" id="s-packaging-your-app">
<span id="packaging-your-app"></span><h2>Packaging your app<a class="headerlink" href="#packaging-your-app" title="Permalink to this headline">¶</a></h2>
<p>Python <em>packaging</em> refers to preparing your app in a specific format that can
be easily installed and used. Django itself is packaged very much like
this. For a small app like polls, this process isn&#8217;t too difficult.</p>
<ol class="arabic">
<li><p class="first">First, create a parent directory for <code class="docutils literal"><span class="pre">polls</span></code>, outside of your Django
project. Call this directory <code class="docutils literal"><span class="pre">django-polls</span></code>.</p>
<div class="admonition-choosing-a-name-for-your-app admonition">
<p class="first admonition-title">Choosing a name for your app</p>
<p>When choosing a name for your package, check resources like PyPI to avoid
naming conflicts with existing packages. It&#8217;s often useful to prepend
<code class="docutils literal"><span class="pre">django-</span></code> to your module name when creating a package to distribute.
This helps others looking for Django apps identify your app as Django
specific.</p>
<p class="last">Application labels (that is, the final part of the dotted path to
application packages) <em>must</em> be unique in <a class="reference internal" href="../../ref/settings/#std:setting-INSTALLED_APPS"><code class="xref std std-setting docutils literal"><span class="pre">INSTALLED_APPS</span></code></a>.
Avoid using the same label as any of the Django <a class="reference internal" href="../../ref/contrib/"><span class="doc">contrib packages</span></a>, for example <code class="docutils literal"><span class="pre">auth</span></code>, <code class="docutils literal"><span class="pre">admin</span></code>, or
<code class="docutils literal"><span class="pre">messages</span></code>.</p>
</div>
</li>
<li><p class="first">Move the <code class="docutils literal"><span class="pre">polls</span></code> directory into the <code class="docutils literal"><span class="pre">django-polls</span></code> directory.</p>
</li>
<li><p class="first">Create a file <code class="docutils literal"><span class="pre">django-polls/README.rst</span></code> with the following contents:</p>
<div class="highlight-default snippet"><div class="snippet-filename">django-polls/README.rst</div>
<div class="highlight"><pre><span></span>=====
Polls
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the &quot;docs&quot; directory.

Quick start
-----------

1. Add &quot;polls&quot; to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        &#39;polls&#39;,
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r&#39;^polls/&#39;, include(&#39;polls.urls&#39;)),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you&#39;ll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
</pre></div>
</div>
</li>
<li><p class="first">Create a <code class="docutils literal"><span class="pre">django-polls/LICENSE</span></code> file. Choosing a license is beyond the
scope of this tutorial, but suffice it to say that code released publicly
without a license is <em>useless</em>. Django and many Django-compatible apps are
distributed under the BSD license; however, you&#8217;re free to pick your own
license. Just be aware that your licensing choice will affect who is able
to use your code.</p>
</li>
<li><p class="first">Next we&#8217;ll create a <code class="docutils literal"><span class="pre">setup.py</span></code> file which provides details about how to
build and install the app.  A full explanation of this file is beyond the
scope of this tutorial, but the <a class="reference external" href="https://setuptools.readthedocs.io/en/latest/">setuptools docs</a> have a good
explanation. Create a file <code class="docutils literal"><span class="pre">django-polls/setup.py</span></code> with the following
contents:</p>
<div class="highlight-default snippet"><div class="snippet-filename">django-polls/setup.py</div>
<div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">from</span> <span class="nn">setuptools</span> <span class="k">import</span> <span class="n">find_packages</span><span class="p">,</span> <span class="n">setup</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="vm">__file__</span><span class="p">),</span> <span class="s1">&#39;README.rst&#39;</span><span class="p">))</span> <span class="k">as</span> <span class="n">readme</span><span class="p">:</span>
    <span class="n">README</span> <span class="o">=</span> <span class="n">readme</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

<span class="c1"># allow setup.py to be run from any path</span>
<span class="n">os</span><span class="o">.</span><span class="n">chdir</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normpath</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="vm">__file__</span><span class="p">),</span> <span class="n">os</span><span class="o">.</span><span class="n">pardir</span><span class="p">)))</span>

<span class="n">setup</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s1">&#39;django-polls&#39;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s1">&#39;0.1&#39;</span><span class="p">,</span>
    <span class="n">packages</span><span class="o">=</span><span class="n">find_packages</span><span class="p">(),</span>
    <span class="n">include_package_data</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">license</span><span class="o">=</span><span class="s1">&#39;BSD License&#39;</span><span class="p">,</span>  <span class="c1"># example license</span>
    <span class="n">description</span><span class="o">=</span><span class="s1">&#39;A simple Django app to conduct Web-based polls.&#39;</span><span class="p">,</span>
    <span class="n">long_description</span><span class="o">=</span><span class="n">README</span><span class="p">,</span>
    <span class="n">url</span><span class="o">=</span><span class="s1">&#39;https://www.example.com/&#39;</span><span class="p">,</span>
    <span class="n">author</span><span class="o">=</span><span class="s1">&#39;Your Name&#39;</span><span class="p">,</span>
    <span class="n">author_email</span><span class="o">=</span><span class="s1">&#39;yourname@example.com&#39;</span><span class="p">,</span>
    <span class="n">classifiers</span><span class="o">=</span><span class="p">[</span>
        <span class="s1">&#39;Environment :: Web Environment&#39;</span><span class="p">,</span>
        <span class="s1">&#39;Framework :: Django&#39;</span><span class="p">,</span>
        <span class="s1">&#39;Framework :: Django :: X.Y&#39;</span><span class="p">,</span>  <span class="c1"># replace &quot;X.Y&quot; as appropriate</span>
        <span class="s1">&#39;Intended Audience :: Developers&#39;</span><span class="p">,</span>
        <span class="s1">&#39;License :: OSI Approved :: BSD License&#39;</span><span class="p">,</span>  <span class="c1"># example license</span>
        <span class="s1">&#39;Operating System :: OS Independent&#39;</span><span class="p">,</span>
        <span class="s1">&#39;Programming Language :: Python&#39;</span><span class="p">,</span>
        <span class="c1"># Replace these appropriately if you are stuck on Python 2.</span>
        <span class="s1">&#39;Programming Language :: Python :: 3&#39;</span><span class="p">,</span>
        <span class="s1">&#39;Programming Language :: Python :: 3.4&#39;</span><span class="p">,</span>
        <span class="s1">&#39;Programming Language :: Python :: 3.5&#39;</span><span class="p">,</span>
        <span class="s1">&#39;Topic :: Internet :: WWW/HTTP&#39;</span><span class="p">,</span>
        <span class="s1">&#39;Topic :: Internet :: WWW/HTTP :: Dynamic Content&#39;</span><span class="p">,</span>
    <span class="p">],</span>
<span class="p">)</span>
</pre></div>
</div>
</li>
<li><p class="first">Only Python modules and packages are included in the package by default. To
include additional files, we&#8217;ll need to create a <code class="docutils literal"><span class="pre">MANIFEST.in</span></code> file. The
setuptools docs referred to in the previous step discuss this file in more
details. To include the templates, the <code class="docutils literal"><span class="pre">README.rst</span></code> and our <code class="docutils literal"><span class="pre">LICENSE</span></code>
file, create a file <code class="docutils literal"><span class="pre">django-polls/MANIFEST.in</span></code> with the following
contents:</p>
<div class="highlight-default snippet"><div class="snippet-filename">django-polls/MANIFEST.in</div>
<div class="highlight"><pre><span></span><span class="n">include</span> <span class="n">LICENSE</span>
<span class="n">include</span> <span class="n">README</span><span class="o">.</span><span class="n">rst</span>
<span class="n">recursive</span><span class="o">-</span><span class="n">include</span> <span class="n">polls</span><span class="o">/</span><span class="n">static</span> <span class="o">*</span>
<span class="n">recursive</span><span class="o">-</span><span class="n">include</span> <span class="n">polls</span><span class="o">/</span><span class="n">templates</span> <span class="o">*</span>
</pre></div>
</div>
</li>
<li><p class="first">It&#8217;s optional, but recommended, to include detailed documentation with your
app. Create an empty directory <code class="docutils literal"><span class="pre">django-polls/docs</span></code> for future
documentation. Add an additional line to <code class="docutils literal"><span class="pre">django-polls/MANIFEST.in</span></code>:</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="n">recursive</span><span class="o">-</span><span class="n">include</span> <span class="n">docs</span> <span class="o">*</span>
</pre></div>
</div>
<p>Note that the <code class="docutils literal"><span class="pre">docs</span></code> directory won&#8217;t be included in your package unless
you add some files to it. Many Django apps also provide their documentation
online through sites like <a class="reference external" href="https://readthedocs.org">readthedocs.org</a>.</p>
</li>
<li><p class="first">Try building your package with <code class="docutils literal"><span class="pre">python</span> <span class="pre">setup.py</span> <span class="pre">sdist</span></code> (run from inside
<code class="docutils literal"><span class="pre">django-polls</span></code>). This creates a directory called <code class="docutils literal"><span class="pre">dist</span></code> and builds your
new package, <code class="docutils literal"><span class="pre">django-polls-0.1.tar.gz</span></code>.</p>
</li>
</ol>
<p>For more information on packaging, see Python&#8217;s <a class="reference external" href="https://packaging.python.org/en/latest/distributing.html">Tutorial on Packaging and
Distributing Projects</a>.</p>
</div>
<div class="section" id="s-using-your-own-package">
<span id="using-your-own-package"></span><h2>Using your own package<a class="headerlink" href="#using-your-own-package" title="Permalink to this headline">¶</a></h2>
<p>Since we moved the <code class="docutils literal"><span class="pre">polls</span></code> directory out of the project, it&#8217;s no longer
working. We&#8217;ll now fix this by installing our new <code class="docutils literal"><span class="pre">django-polls</span></code> package.</p>
<div class="admonition-installing-as-a-user-library admonition">
<p class="first admonition-title">Installing as a user library</p>
<p>The following steps install <code class="docutils literal"><span class="pre">django-polls</span></code> as a user library. Per-user
installs have a lot of advantages over installing the package system-wide,
such as being usable on systems where you don&#8217;t have administrator access
as well as preventing the package from affecting system services and other
users of the machine.</p>
<p class="last">Note that per-user installations can still affect the behavior of system
tools that run as that user, so <code class="docutils literal"><span class="pre">virtualenv</span></code> is a more robust solution
(see below).</p>
</div>
<ol class="arabic">
<li><p class="first">To install the package, use pip (you already <a class="reference internal" href="#installing-reusable-apps-prerequisites"><span class="std std-ref">installed it</span></a>, right?):</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">--</span><span class="n">user</span> <span class="n">django</span><span class="o">-</span><span class="n">polls</span><span class="o">/</span><span class="n">dist</span><span class="o">/</span><span class="n">django</span><span class="o">-</span><span class="n">polls</span><span class="o">-</span><span class="mf">0.1</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
</pre></div>
</div>
</li>
<li><p class="first">With luck, your Django project should now work correctly again. Run the
server again to confirm this.</p>
</li>
<li><p class="first">To uninstall the package, use pip:</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">uninstall</span> <span class="n">django</span><span class="o">-</span><span class="n">polls</span>
</pre></div>
</div>
</li>
</ol>
</div>
<div class="section" id="s-publishing-your-app">
<span id="publishing-your-app"></span><h2>Publishing your app<a class="headerlink" href="#publishing-your-app" title="Permalink to this headline">¶</a></h2>
<p>Now that we&#8217;ve packaged and tested <code class="docutils literal"><span class="pre">django-polls</span></code>, it&#8217;s ready to share with
the world! If this wasn&#8217;t just an example, you could now:</p>
<ul class="simple">
<li>Email the package to a friend.</li>
<li>Upload the package on your website.</li>
<li>Post the package on a public repository, such as <a class="reference external" href="https://pypi.python.org/pypi">the Python Package Index
(PyPI)</a>. <a class="reference external" href="https://packaging.python.org">packaging.python.org</a> has <a class="reference external" href="https://packaging.python.org/en/latest/distributing.html#uploading-your-project-to-pypi">a good
tutorial</a>
for doing this.</li>
</ul>
</div>
<div class="section" id="s-installing-python-packages-with-virtualenv">
<span id="installing-python-packages-with-virtualenv"></span><h2>Installing Python packages with virtualenv<a class="headerlink" href="#installing-python-packages-with-virtualenv" title="Permalink to this headline">¶</a></h2>
<p>Earlier, we installed the polls app as a user library. This has some
disadvantages:</p>
<ul class="simple">
<li>Modifying the user libraries can affect other Python software on your system.</li>
<li>You won&#8217;t be able to run multiple versions of this package (or others with
the same name).</li>
</ul>
<p>Typically, these situations only arise once you&#8217;re maintaining several Django
projects. When they do, the best solution is to use <a class="reference external" href="https://virtualenv.pypa.io/">virtualenv</a>. This tool allows you to maintain multiple
isolated Python environments, each with its own copy of the libraries and
package namespace.</p>
</div>
</div>

</div>



<div class="browse-horizontal">
  
  <div class="left"><a href="../tutorial07/"><i class="icon icon-chevron-left"></i> Writing your first Django app, part 7</a></div>
  
  
  <div class="right"><a href="../whatsnext/">What to read next <i class="icon icon-chevron-right"></i></a></div>
  
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
          Maciej Gryka donated to the Django Software Foundation to
          support Django development. Donate today!
        </a></li>
      </ul>
    </div>
  </div>



  
    <h2>Contents</h2>
    
    <ul>
<li><a class="reference internal" href="#">Advanced tutorial: How to write reusable apps</a><ul>
<li><a class="reference internal" href="#reusability-matters">Reusability matters</a></li>
<li><a class="reference internal" href="#your-project-and-your-reusable-app">Your project and your reusable app</a></li>
<li><a class="reference internal" href="#installing-some-prerequisites">Installing some prerequisites</a></li>
<li><a class="reference internal" href="#packaging-your-app">Packaging your app</a></li>
<li><a class="reference internal" href="#using-your-own-package">Using your own package</a></li>
<li><a class="reference internal" href="#publishing-your-app">Publishing your app</a></li>
<li><a class="reference internal" href="#installing-python-packages-with-virtualenv">Installing Python packages with virtualenv</a></li>
</ul>
</li>
</ul>

    
  

  
  <h2>Browse</h2>
  <ul>
    
    
    <li>Prev: <a href="../tutorial07/">Writing your first Django app, part 7</a></li>
    
    
    <li>Next: <a href="../whatsnext/">What to read next</a></li>
    
    <li><a href="https://docs.djangoproject.com/en/1.11/contents/">Table of contents</a></li>
    
    <li><a href="https://docs.djangoproject.com/en/1.11/genindex/">General Index</a></li>
    
    <li><a href="https://docs.djangoproject.com/en/1.11/py-modindex/">Python Module Index</a></li>
    
    
  </ul>
  

  
  <h2>You are here:</h2>
  <ul>
    <li>
      <a href="https://docs.djangoproject.com/en/1.11/">Django 1.11 documentation</a>
      
      <ul><li><a href="../">Getting started</a>
      
      <ul><li>Advanced tutorial: How to write reusable apps</li></ul>
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
