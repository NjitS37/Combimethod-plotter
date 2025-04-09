import subprocess
import os
import matplotlib.pyplot as plt
import numpy as np

# Constants
hashlist = "minecraftcleartext.txt"
rockyoupcfg = "Largerockyou.txt"  # PCFG Rockyou list of length end_loop - step
rockyou = "rockyou.txt"
wordlist = "minecraftscrape.txt"
llamalist = "minecraftllama3110000_results.txt"
philist = "Minecraftphi4.txt"
hashcat_mode = "99999"
attack_mode = "0"
outfile = "cracked.txt"
plot_filename = "minecraftcombirockyouscrapellamaphi.png"  # The saved plot filename
rule_name = "OneRuleToRuleThemStill.rule"
N = 292115 # Lengte van woordnelijst

# Storage for results
x_values = [0]  # Wordlist size
y_values = [0]  # Passwords cracked
total_cracked = 0

start_rockyou = 1_000_000
end_rockyouloop = 11_000_000
step_rockyou = 1_000_000


# Loop over wordlist sizes (1M to 10M, step 1M), PCFG rockyou lijst
for lines in range(start_rockyou, end_rockyouloop, step_rockyou):
    temp_wordlist = f"temp_wordlist_{lines}.txt"

    # Extract first 'lines' lines into a temporary wordlist
    subprocess.run(f"head -n {lines} {rockyoupcfg} > {temp_wordlist}", shell=True)

    # Clear any previous cracked.txt results
    if os.path.exists(outfile):
        os.remove(outfile)

    # Run PCFG rockyou hashcat
    subprocess.run(
        f"hashcat -m {hashcat_mode} -a {attack_mode} {hashlist} {temp_wordlist} --outfile={outfile} --outfile-format=2 --quiet --remove",
        shell=True
    )
    
    # Count cracked passwords
    with open(outfile, "r") as f:
        cracked_count = sum(1 for _ in f)
    
    total_cracked += cracked_count

    # Store results
    x_values.append(lines)
    y_values.append(total_cracked)

    print(f"Rockyou Size: {lines}, Passwords Cracked: {cracked_count}")

"""
# Loop over wordlist sizes (1M to 10M, step 1M), Rockyou met rules
for lines in range(start_rockyou, 15000000, step_rockyou):
    temp_wordlist = f"temp_wordlist_{lines}.txt"

    # Extract first 'lines' lines into a temporary wordlist
    subprocess.run(f"head -n {lines} {rockyou} > {temp_wordlist}", shell=True)

    # Clear any previous cracked.txt results
    if os.path.exists(outfile):
        os.remove(outfile)

    # Run PCFG rockyou hashcat
    subprocess.run(
        f"hashcat -m {hashcat_mode} -a {attack_mode} {hashlist} {temp_wordlist} -r {rule_name} --outfile={outfile} --outfile-format=2 --quiet --remove",
        shell=True
    )
    
    # Count cracked passwords
    with open(outfile, "r") as f:
        cracked_count = sum(1 for _ in f)
    
    total_cracked += cracked_count

    # Store results
    x_values.append(lines)
    y_values.append(total_cracked)

    print(f"Rockyou Size: {lines}, Passwords Cracked: {cracked_count}")
"""

# Storage for results
maxpcfgx = max(x_values)
maxpcfgy = max(y_values)
x_valuesscrape = [maxpcfgx]
y_valuesscrape = [maxpcfgy]

start_scrape = 1000
end_scrapeloop = 11000
step_scrape = 1000

# Nu schakelen we over naar de scraper om te kijken of er een bump toegevoegd kan worden.
for lines in range(start_scrape, end_scrapeloop, step_scrape):
    temp_wordlist = f"temp_wordlist_{lines}.txt"

    # Extract first 'lines' lines into a temporary wordlist
    subprocess.run(f"head -n {lines} {wordlist} > {temp_wordlist}", shell=True)

    # Clear any previous cracked.txt results
    if os.path.exists(outfile):
        os.remove(outfile)

    # Run PCFG rockyou hashcat
    subprocess.run(
        f"hashcat -m {hashcat_mode} -a {attack_mode} {hashlist} {temp_wordlist} -r {rule_name} --outfile={outfile} --outfile-format=2 --quiet --remove",
        shell=True
    )
    
    
    # Count cracked passwords
    with open(outfile, "r") as f:
        cracked_count = sum(1 for _ in f)
    
    total_cracked += cracked_count

    # Store results
    x_valuesscrape.append(maxpcfgx + 1000*lines)
    y_valuesscrape.append(total_cracked)

    print(f"Wordlist Size: {lines}, Passwords Cracked: {cracked_count}")
    
    
# Storage for results
maxscrapex = max(x_valuesscrape)
maxscrapey = max(y_valuesscrape)
x_valuesllama = [maxscrapex]
y_valuesllama = [maxscrapey]

# Nu schakelen we over naar llama
for lines in range(start_scrape, end_scrapeloop, step_scrape):
    temp_wordlist = f"temp_wordlist_{lines}.txt"

    # Extract first 'lines' lines into a temporary wordlist
    subprocess.run(f"head -n {lines} {llamalist} > {temp_wordlist}", shell=True)

    # Clear any previous cracked.txt results
    if os.path.exists(outfile):
        os.remove(outfile)

    # Run PCFG rockyou hashcat
    subprocess.run(
        f"hashcat -m {hashcat_mode} -a {attack_mode} {hashlist} {temp_wordlist} -r {rule_name} --outfile={outfile} --outfile-format=2 --quiet --remove",
        shell=True
    )
    
    
    # Count cracked passwords
    with open(outfile, "r") as f:
        cracked_count = sum(1 for _ in f)
    
    total_cracked += cracked_count

    # Store results
    x_valuesllama.append(maxscrapex + 1000*lines)
    y_valuesllama.append(total_cracked)

    print(f"Wordlist Size: {lines}, Passwords Cracked: {cracked_count}")


# Storage for results
maxllamax = max(x_valuesllama)
maxllamay = max(y_valuesllama)
x_valuesphi = [maxllamax]
y_valuesphi = [maxllamay]

# Nu schakelen we over naar llama
for lines in range(start_scrape, end_scrapeloop, step_scrape):
    temp_wordlist = f"temp_wordlist_{lines}.txt"

    # Extract first 'lines' lines into a temporary wordlist
    subprocess.run(f"head -n {lines} {philist} > {temp_wordlist}", shell=True)

    # Clear any previous cracked.txt results
    if os.path.exists(outfile):
        os.remove(outfile)

    # Run PCFG rockyou hashcat
    subprocess.run(
        f"hashcat -m {hashcat_mode} -a {attack_mode} {hashlist} {temp_wordlist} -r {rule_name} --outfile={outfile} --outfile-format=2 --quiet --remove",
        shell=True
    )
    
    
    # Count cracked passwords
    with open(outfile, "r") as f:
        cracked_count = sum(1 for _ in f)
    
    total_cracked += cracked_count

    # Store results
    x_valuesphi.append(maxllamax + 1000*lines)
    y_valuesphi.append(total_cracked)

    print(f"Wordlist Size: {lines}, Passwords Cracked: {cracked_count}")



plt.figure(figsize=(10, 6))
plt.plot(x_values, (np.array(y_values)/N)*100, marker='o', linestyle='-', color='b', label='Rockyou PCFG')
plt.plot(x_valuesscrape, (np.array(y_valuesscrape)/N)*100, marker='o', linestyle='-', color = 'r', label='Wikiscraper with OneRule')
plt.plot(x_valuesllama, (np.array(y_valuesllama)/N)*100, marker='o', linestyle='-', color = 'g', label='Llama3.1 with OneRule')
plt.plot(x_valuesphi, (np.array(y_valuesphi)/N)*100, marker='o', linestyle='-', color = 'm', label='Phi4 with OneRule')
plt.xlabel("List size of method")
plt.ylabel("Percentage of passwords cracked (%)")
plt.title("Hashcat cracking performance for multiple methods for the Planetminecraft leak")
plt.grid(True)
plt.legend()

# Define x-tick positions:
# 0M to 10M
xticks = [i * 1_000_000 for i in range(0, 11)]
xtick_labels = [f"{i}M" for i in range(0, 11)]

# 1k to 10k placed at positions where 11M to 20M would be
xticks += [10_000_000 + i * 1_000_000 for i in range(1, 11)]
xtick_labels += [f"{i}k" for i in range(1, 11)]

xticks += [20_000_000 + i * 1_000_000 for i in range(1, 11)]
xtick_labels += [f"{i}k" for i in range(1, 11)]

xticks += [30_000_000 + i * 1_000_000 for i in range(1, 11)]
xtick_labels += [f"{i}k" for i in range(1, 11)]

# Apply to plot
plt.xticks(xticks, xtick_labels, rotation=45)

plt.tight_layout()
plt.savefig(plot_filename, dpi=300)
print(f"Plot saved as {plot_filename}")
