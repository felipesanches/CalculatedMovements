Reimplementation of some of the scenes in "Calculated Movements" by Larry Cuba, 1982-1985
----

A video-recording of the original is available here:

https://www.youtube.com/watch?v=OkyqP-g_LrY

The original animation was implemented using the ZGRASS programming language on a Datamax UV1 computer.

This reimplementation in Python with Processing was written by Felipe Corrêa da Silva Sanches <juca@members.fsf.org> and is released to the public domain.

For now, we're using the original audio and only reimplementing the visuals.
Later we could perhaps use SuperCollider or something similar to also reimplement the music and sound effects.

October 25th, 2021

**Note:** The font file 3270Condensed-Regular.otf created by my friend RBanffy was copied from its Debian package. Learn more about this font family at https://github.com/rbanffy/3270font

How to run this!
----

On Debian GNU+Linux I did it this way:

* sudo apt install virtualenv openjdk-11-jre
* virtualenv venv -ppython3
* . venv/bin/activate
* pip install -r requirements.txt
* python CalculatedMovements.py

On other systems, please adapt the above instructions. I'd be surely happy to merge PRs with additional instructions.
