<!DOCTYPE html>

<html lang="en" data-content_root="./">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
  </head>
<body>

  <section id="getting-started">
<h1>Getting Started<a class="headerlink" href="#getting-started" title="Link to this heading"></a></h1>
<div class="toctree-wrapper compound">
</div>
</section>
<section id="requirements">
<h1>Requirements<a class="headerlink" href="#requirements" title="Link to this heading"></a></h1>
<ul class="simple">
<li><p>Python 3.9 or newer</p></li>
<li><p>pywin32</p></li>
<li><p>numpy</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>To install pywin32, open command prompt and type:</p>
<div class="literal-block-wrapper docutils container" id="id1">
<div class="code-block-caption"><span class="caption-text">Windows Command Prompt</span><a class="headerlink" href="#id1" title="Link to this code"></a></div>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">   pip install pywin32</span>
</pre></div>
</div>
</div>
<p>Or if using Anaconda:</p>
<div class="literal-block-wrapper docutils container" id="id2">
<div class="code-block-caption"><span class="caption-text">Windows Command Prompt</span><a class="headerlink" href="#id2" title="Link to this code"></a></div>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">   conda install -c anaconda pywin32</span>
</pre></div>
</div>
</div>
</div>
</section>
<section id="installing-fewrap">
<h1>Installing fewrap<a class="headerlink" href="#installing-fewrap" title="Link to this heading"></a></h1>
<p>To use this module, place this folder in the \Lib folder of your Python installation directory to be able to use it in
any project.</p>
</section>
<section id="translating-femap-api-to-python">
<h1>Translating FEMAP API to Python<a class="headerlink" href="#translating-femap-api-to-python" title="Link to this heading"></a></h1>
<div class="admonition important">
<p class="admonition-title">Important</p>
<p>If you’ve never used Python with the FEMAP API before, you’ll need to transfer the FEMAP API type library into
something Python can read.</p>
<p>We do this by generating a new file called <strong>Pyfemap.py</strong>.</p>
</div>
<section id="how-to-auto-generate-pyfemap-py">
<h2>How to auto-generate Pyfemap.py<a class="headerlink" href="#how-to-auto-generate-pyfemap-py" title="Link to this heading"></a></h2>
<p>To generate this file, we utilize the <em>makepy</em> function from the pywin32 module. The necessary code is included
in this module and is located within the <em>setup_pyfemap.py</em> file.</p>
<ol class="arabic simple">
<li><p>Run the setup_pyfemap.py file and follow the GUI instructions to select the <em>femap.tlb</em> file</p></li>
</ol>
<div class="admonition hint">
<p class="admonition-title">Hint</p>
<p>This should be in the same directory where your <em>femap.exe</em> is located</p>
</div>
<ol class="arabic simple" start="2">
<li><p>A new file should be created in your \Lib folder in your Python installation directory titled <em>Pyfemap.py</em>.
You can move this file if you wish to another location if you want more control over your package dependencies.</p></li>
</ol>
<ol class="arabic simple" start="5">
<li><p>You’re done! You should be able to open an interactive Python shell and import Pyfemap without any errors</p></li>
</ol>
<blockquote>
<div><div class="literal-block-wrapper docutils container" id="id3">
<div class="code-block-caption"><span class="caption-text">Python Shell</span><a class="headerlink" href="#id3" title="Link to this code"></a></div>
<div class="highlight-Python notranslate"><div class="highlight"><pre><span></span>   <span class="kn">import</span> <span class="nn">Pyfemap</span>
</pre></div>
</div>
</div>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If you ever upgrade to a newer version of Python or FEMAP, you should re-run this script. Otherwise, once it’s
installed, you’re good to go.</p>
</div>
</section>
</section>
<section id="connecting-to-femap">
<h1>Connecting to FEMAP<a class="headerlink" href="#connecting-to-femap" title="Link to this heading"></a></h1>
<p>Now that you have translated the FEMAP API Type Library into Pyfemap.py, let’s connect to FEMAP.</p>
<p>The first thing that you must do before you can use any of the other functionality in the FEMAP API is to access the
FEMAP model, or application object. This object provides access to all of the other methods and properties, including
the methods used to create other model objects.</p>
<p>Connecting to an active FEMAP session is accomplished via OLE/COM between Python and FEMAP. This is done by interacting
with the FEMAP Application object.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If you’re familiar with the FEMAP API in VBA, this is commonly referred to as <em>App</em>.
We will be referring to this object as simply <em>femap</em>, but of course you can call it whatever you’d like.</p>
</div>
<p>When you define your <em>femap</em> object, you usually will want to make it global, or available to your entire program.
Once you ‘get’ or ‘create’ the object, the existence of this object serves as your connection to FEMAP. In most cases,
you will not want to repeatedly create and destroy this object.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>You will see that the femap object is passed as a parameter to many of the functions listed in this module, but
does not return a ‘new’ femap object. This is by design as arguments are passed by <em>assignment</em> in Python.</p>
<p>That is, the parameter passed is actually a <em>reference</em> to the object. Since our object is <em>mutable</em>, meaning we can
change it’s state, any changes we make to it are visible to the outer scope.</p>
</div>
<p>To get this object, the necessary code is contained in the function <a class="reference internal" href="connect.html#connect-to-femap"><span class="std std-ref">connect_to_femap()</span></a></p>
<div class="literal-block-wrapper docutils container" id="id4">
<div class="code-block-caption"><span class="caption-text">Python Shell</span><a class="headerlink" href="#id4" title="Link to this code"></a></div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="c1"># This opens a new model</span>
<span class="kn">from</span> <span class="nn">fewrap</span> <span class="kn">import</span> <span class="n">connect_to_femap</span>
<span class="n">femap</span> <span class="o">=</span> <span class="n">connect_to_femap</span><span class="p">()</span>
</pre></div>
</div>
</div>
<p>You will see a message in your console and in your FEMAP messages window confirming that you are connected.</p>
</section>

  </body>
</html>