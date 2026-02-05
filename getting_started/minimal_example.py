import webbrowser
from pathlib import Path

from qibocal import create_calibration_platform
from qibocal.protocols import rabi_amplitude

# ----------------------------------------------------
# ADDITIONAL STEPS TAKEN TO MAKE THIS SCRIPT WORK:
# ----------------------------------------------------
# 1) Set up the env var that points to the platforms
# import os
# os.environ['QIBOLAB_PLATFORMS'] = './platforms' # Add here for temporarily setting it OR
# If you may want to make the above permanent type in terminal:
# > nano ~/.zshrc
# > export QIBOLAB_PLATFORMS=/Users/elis/Desktop/PROJECTS/Quantum/qibocal/platforms
# > source ~/.zshrc
#
# 2) Line platform = create_calibration_platform("qubit") failing because of wrong syntax of file
# platforms/qubit/parameters.json. Inside 'hamiltonian' section "qubits" --> "single_qubit"
#
# 3) Line: plots, table = rabi_amplitude.report(data=data, fit=results, target=targets[0])
#    'fit=' previously wrong 'results='' , and, typo 'target[0]--> 'targetS[0]'
#
# 4) Line plots[0].show(renderer="browser") added the renderer="browser" otherwise not working for me.
# 5) Added imports


# create platform
platform = create_calibration_platform("qubit")

# define qubits where the protocols will be executed
targets = [0]

# define protocol parameters
params = rabi_amplitude.parameters_type.load(
    dict(
        min_amp=0.01,
        max_amp=0.2,
        step_amp=0.02,
        nshots=2000,
        pulse_length=40,
    )
)

# acquire
platform.connect()
data, acquisition_time = rabi_amplitude.acquisition(
    params=params, platform=platform, targets=targets
)
platform.disconnect()

# post-processing
results, fit_time = rabi_amplitude.fit(data=data)

# visualize the results
plots, table = rabi_amplitude.report(data=data, fit=results, target=targets[0])
# plots[0].show(renderer="browser")

# from IPython import display
# display.HTML(table)


# make plot smaller
plots[0].update_layout(height=600)

html_file = Path("rabi_demo.html")
plots[0].write_html(html_file, include_plotlyjs="cdn")

with open(html_file, "a") as f:
    f.write(table)

webbrowser.open(html_file.resolve().as_uri())
