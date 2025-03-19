# SecureGPGWebbApp
This is a secure web application project exploring the GPG mechanics for user data, content and communication encryption.

## Basic idea
1. Users provide their own PGP keys to encrypt their content.
2. Users are identified solely based on their PGP keys.
1. They define their own friends (users they trust) by exchanging PGP keys
1. Users can only view content that is public, or published by a person they have in their list of friends (entrusted PGP keys)
   2. Here is a tricky part. It is explained more in the (section about limited accessibility)[#private_posts]
   3. This shit is not yet implemented and is a subject of a personal research.
1. The web application deffers the encryption to the user's machine
   so that there is no requirement actually share the private key with the service provider.
   This feature is not realised yet (TODO: find out how to do this in browsers)

# Glossary

- **Leaker** – a user account that leaks information to the unintended audience
- **Creator** – a user account that provides content to the intended audience using the tools provided by the application framework
- **leak event** – a situation, when a user account shares information with unintended audience

# Private posts

The basic idea is to utilise PGP keys to share posts to a limited amount of people.
What follows is a first iteration of this idea, which is not based on any relevant literature as I am writing this without internet on a plane.
There are multiple applicable approaches, which have multiple safety benefits. 
In any cas, the basic requirement is to have a web application with user account that allows for publishing posts from user accounts (any stabdard blog web app)
and to have the user accounts require a PGP key.
There is always a user account, let's call him/her **Creator**, who publishes posts and requires,
that only the users **U_1**, **U_2**, ..., **U_n** can see and decipher the posts.


## Naive broadcast

### Schema

1. The Creator creates a dedicated "Group key pair" (**G_pub**, **G_priv**),
   and shares the **G_pub** only with the group of users he wants to be able to decipher the posts.
2. Creator encrypts the post using **G_priv** and lets anyone access the encrypted post.

### Limitations

It only takes a single insider, lets call him/her a **Leaker**, to leak the public key and expose the full set posts encrypted by the single private key.
There is no way of telling who leaked the public key and therefore there can't be any repercussions.
It is not safe to share a new key with the same pool of users because it is impossible to identify the Leaker account.

### Benefits

Simple to implement, only a single key pair to manage.

## Naive Private broadcast

1. **Creator** collects public keys from each of the users **U1**, **U2**, ..., **Un**,
   denoted **K1_pub**, **K2_pub**, ..., **Kn_pub** and encrypts the content using each of the public keys.
2. Each of the encrypted versions is stored on the server to be served to the respective users, based on the public key fingerprint.
2. Each user can only decrypt the instance of the post encrypted by his/her public key using his/her private key.

### Limitations

There needs to be **n** copies of the same content stored on the server,
each one encrypted by a different public key.
Here, to identify the **Leaker**, it is necessary to share different versions of the information with each user account and match it with the leaked information.
This may be harder with each additional **Leaker** but it allows for some form of security.

### Benefits

If a known subset of accounts is deemed trusted despite the **leak event**,
the  next post can be share only with the subset of the accounts, 
only requiring to modify the list of public keys to encrypt the content with.

## Reduced Private Broadcast

Improving on the idea of (naive private broadcast)[#naive_private_broadcast], 
this method reduces the space required for the stored content. 
It leverages cryptography to only store encryptions of a key instead of the multiple encrypted versions of the content.

1. **Creator** picks a random, one-time-use key pair (**P_pub**, **P_priv**) and encrypts the post using **P_priv** to get the encrypted content.
2. then, **Creator** encrypts **P_pub** separately using public keys of the intended recipients **U1**, **U2**, ..., **Un** 
   to obtain encrypted version of **P_pub** **K1_pub**, **K2_pub**, ..., **Kn_pub**. 
3. All encryptions **K1_pub**, **K2_pub**, ..., **Kn_pub** are added to the post for the intended users to decrypt 
   and obtain the **P_pub** key to decrypt the main post.


### Limitations

None really.

### Benefits

The storage requirements for a post grows independently of its size, 
only requiring one encrypted version of the post and **n** encrypted verions of the master, one-time-use key **P_pub** 
(which is potentially less than **n** encryptions of a large post with images)






