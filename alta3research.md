# STEPS TO SECURILY AND EFFICIENTLY CONNECT TO GITHUB USING SSH
PATs (Personal Access Tokens), essentially long passwords attached to an account and regular passwords use basic password authentication over HTTPS.
They are both vulnerable to brute-force attacks and run the risk of being abused in a case of a data breach.
Using SSH is more secure because it uses stronger encryption and public-key authentication is better than basic auth over HTTPS.
Using SSH also enables passwordless auth out of the box.

## PRE-REQ
Create repository on Github.
    - Github is basically a 'remote Git server', i.e. a computer in the cloud (accessible over the internet) to store files
    - A repository can be thought of as a folder/directory on our Git server

## STEPS
1. On the local machine, use ssh-keygen command to generate a private-public key pair
    CMD: ssh-keygen -t ed25519 -C "your_email@example.com"
    The -t specifies the type of encryption algorithm to use for the asymetric key generation
    The -C specifies the label to use for the keys (to easily identify them)

2. Establish trust between Git server (GitHub) and client (local machine)
    - Copy the id_ed25519.pub key content and add it to Github (Profile Settings -> SSH and GPG Keys -> New SSH key
    - Verify connection by running ssh -T git@github.com
        - If you don't get shown Github's host key fingerprint (a short, hashed version of its host public key), you might need to edit your ~/.ssh/config file. Make sure that ssh is looking for the right key file (say id_ed25519 instead of id_rsa file)
    - When prompted to continue, don't just enter yes. Make sure the fingreprint is authentically coming from Github server. If not, you are under a man-in-the-middle attack. To verify that the fingerprint is legit, a quick 'Github fingeprint' should get you to the right place.
    - If the fingerprint is authentic, type yes and hit Enter to close the 2-way trust relationship between your local machine (Git client) and GitHub (Git server). Essentially, ssh stores the fingerprint of the server you trust in the ~/.ssh/known_hosts (akin to how you stored your public key on Github telling it to trust the computer with your private key)

3. With the trust established, time to clone (or update remote repo connection if already cloned) using the SSH url instead of the HTTPS one.

4. From here on out, pushing or pulling code from GitHub should be secure and passwordless. If you locked your SSH key with a passphrase, you will have to enter that. But this is different from, sending your password over the wire.

## BONUS
This SSH auth workflow can also be used to enable CI/CD automation, thanks to the secure and passwordless benefits. Look into setting up "Deploy keys" if interested.

Hope this helps, for more info visit [GitHub official docs]( https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)
