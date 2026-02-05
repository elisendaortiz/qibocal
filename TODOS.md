You need to try out this other example from
here: https://qibo.science/qibocal/stable/getting-started/example.html

````
platform: qw5q_gold

targets: [0]

actions:
    - id: resonator high power high amplitude
      operation: resonator_spectroscopy
      parameters:
          freq_width: 10_000_000
          freq_step: 100_000
          amplitude: 0.4
          power_level: high
          nshots: 1024
```

For that, you probably need to add a new platform
You can probably find it here:
But the idea for correct developing is not that you add this platform to your local platform folder of this branch. The idea is you are able to set up correctly the path of env variable QIBOLAB_PLATFORMS=/Users/elis/Desktop/PROJECTS/Quantum/qibocal/platforms
to point to the platforms that you need that are all in the platforms repo
Repo: https://github.com/qiboteam/qibolab_platforms_qrc

(Remember atm you made 'QIBOLAB_PLATFORMS' permanent in your ~/.zshrc, so need to work out how to sort the new way permanently too and/or remove this current path from ~/.zshrc --it's at the bottom of the file when you nano)


AFTER SOLVING THIS START WITH INSTALLATION AND GETTING STARTED WITH QIBOLAB
Repo: https://github.com/qiboteam/qibolab
Same approach, first example from the readme.md then from the docs.
Docs: https://qibo.science/qibolab/stable/getting-started/experiment.html


Also take a look at the Applications tutorials page to get an idea of examples
Applications: https://qibo.science/qibo/stable/code-examples/applications.html#applications
