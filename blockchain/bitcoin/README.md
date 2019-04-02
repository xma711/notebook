How bitcoin works
-------------------------------

Each bitcoin address is a public key.
Public in the sense that it is open to everyone to view.  
Correspondingly, there is a private key, exactly like the ssh key pair.

Things that are encrypted by the public key can be decrypted by the private key,
and vice versa.

However, given one of the keys, there is no way to get the other key back.

When A wants to sends a BTC to B,
A wrote a file with contents something like "my BTC is from XXX; i want to transfer this BTC to (public) address xxxxxxx".  
Then A encrypts this file with A's private key (no one knows about this key except A).  
A then sends this file to the connected nodes that will verify this file (these nodes are called miners.)

Although none of the nodes knows A's private key, they are able to decrypt A's file using A's public key.

If one malicious node wants to modify the destination address to his address, he has to decrypt the file (no problem),
change the destination address (no problem),
and encrypt using A's private key (PROBLEM! because the malicious node doesn't have A's private key)

why cant the malicious node not encrypt using his own private key?
If this is done, the file cannot be decrypted by A's public key anymore.  
If ppl decrypt the file using the malicious node's public address, then it no longer represents that it is a request from A.

Okay, next is for the nodes to verify.
The basic verification is logically easy.
As this BTC to be sent can be traced all the way to its creation, the verification nodes just have to trace all the way to see if A really has this BTC.

Why do they know the full history?
Because each node has kept a copy of the full history of every single BTC's transactions.

Btw every time we want to know how many BTC a public address (wallet) owns, it is always to look at the full history that has something to do with this address
and deduce the amount this address has.  
Sounds efficient but it is always correct.

Wait, if the verification is so easy, then whose node's verification is accepted?  
One important thing here is that to make sure the node really puts efforts into verification,
the protocol artificially introduces some hard works for them to do.  
If a malicious node wants to approve a malicious transmit request, he can do but he still has to finish this artificial works.  
This is a concept of proof of work.

One example is that if we require each email sender to compute a hash value for the email he wants to send,
the spammers will have to spent a lot of resources if they want to spam a lot of receivers, which reduce their incentive to do so.

In BTC's case, the works required is to find a number (nouce) such that the hash value of the request file A sends and this number has to have enough leading 0s.
This work cannot be solved by any short cut except brute force.
Whoever that is able to come out with a such a number will be the node that POTENTIALLY to the ONLY verifier that all other nodes recognize for this round.

In a simple scenario, if a node comes out with this number much faster than others, it will immediately broadcast this verification to all other nodes.  
The finding of the number is every difficult, but the verification is very easy.
Other nodes will verify if this node really achieves this. if yes, they accept the answer and give up this own trial.
At this point, all nodes update their local copy of the full history of BTC.

What do you mean by "update the history of BTC"?
Actually the history is maintained by a blockchain.
In a blockchain, one block consists of its own information, plus a hash value of the previous block, plus a hash value of all the content. 

Once a verification is accepted by a node, it add this block to the blockchain.

One simplification in the above example is that the node only verifies the transaction from A to B.
But in reality, several unverified transactions are grouped together and verified by a node.
Therefore one block in blockchain is for verification of several transactions (in BTC).  
Of course it doesn't prevent another design to approve one transaction at a time, but it will be extremely inefficient.

On the other hand, why not group even more transactions to one block?
The problem with a too big block is that a more powerful machine will tend to beat a less powerful machine if a block is too big,
which defeats the purpose of decentralization.  
In fact this is a on-going argument inside BTC community.  
Actually BTC has been forked to form BCH, which has a bigger block (ultimately benefit big miners more).

Back to the verification process.
Why miners want to help verify the transactions?  
Because there are rewards.
The miner who is the first to solve the math problem and gets accepted by all other nodes will be rewarded with new BTC.  
The number of of BTC rewarded is halved every 4 years.

What if a malicious node deliberately rejects the new block?
Firstly, he is free to reject but most others will accept anyway.
There is no way for the malicious node to make 51% other nodes to reject the correct block.

Besides, if the malicious node really want to accept a false transaction, he has to come out with a number faster than the whole network.
This is to compete with the whole network's resources, which he unlikely will win.

But let's say he really manages to come out with a number faster than others, so what?
He cannot modify the content of the request file.
If the content itself is malicious (coming form this miner itself), other nodes will reject the block anyway because the content inside is not consistent..

The most difficult scenario is that A sends the BTC to B, and then sends the same BTC to C.
If request 1 is received by one miner only and request 2 is received by 2nd miner only,
from each miner's point of view, the request is correct.

Assume that both miners are equally fast and make their own blocks and then broadcast.
Nearly miners will accept the answer if they only receive one block.
But at some point, some miners will receive 2 versions of the blockchain, one with a history of A sends to B and one with A sends to C.  
The miner just has to accept one of them.
The rule is to accept the blockchain with the longest blocks.  
The thing here is that one transaction is not more correct than the other, so anyone will do.
But the rule is to accept the longest blockchain because it is hardest to recreate the full blockchain
and therefore hardest for any attackers to fake the blockchain.

Whichever transaction is accepted, only one spending from A will be recorded so there is no double-spending problem.

You may ask what if A wants to send it to B but accidentally sends again to C later, but the 2nd request turns out to be accepted by the network?
That's A's problem.
The network maintains one history only.

Btw can one node change part of the history and convince all other nodes to accept the modified history?  
Both are difficult.
To change a few blocks, you need to create the number for each block to fulfill the hash requirement, which is time-consuming.
Though ultimately you may achieve it (after many years of computation maybe), then what?
You need to hack into 51% of nodes that change their blockchains.. quite impossible.

In fact, the double-spending problem seems the most difficult one to solve but BTC's proof of work (POW) manages to solve this.

One more thing is that if more and more nodes joining the mining process, doesn't it mean that the verification process gets faster and faster?

The answer is no. because the protocol adjust the difficulty level of the hashing requirements based on the number of miners.
If more miners, the difficulty level increases.
Ultimately it maintains a same average rate of creation of a new block (one new block every 10 min).

Why do they want this?
This is to make sure if there are more nodes, the security is higher, because each miner is competing with all the others on a more difficult problem.
And the chance that any miner can solve this problem drops.
