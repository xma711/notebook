how bitcoin works
-------------------------------

each bitcoin address is a public key.
public in the sense that it is open to everyone to view.  
correspondingly, there is a private key, exactly like the ssh key pair.

things that are encrypted by the public key can be unencrypted by the private key,
and vice versa.

however, given one of the keys, there is no way to get the other key back.

when A wants to sends a BTC to B,
A wrote a file with contents something like "my BTC is from XXX; i want to transfer this BTC to (public) address xxxxxxx".  
then A encrypts this file with A's private key (no one knows about this key except A).  
A then sends this file to the connected nodes that will verify this file (these nodes are called miners.)

although none of the nodes knows A's private key, they are able to decrypt A's file using A's public key.

if one malicious node wants to modify the destination address to his address, he has to decrypt the file (no problem),
change the destination address (no problem),
and encrypt using A's private key (PROBLEM! because the malicious node doesn't have A's private key)

why cant the malicious node not encrypt using his own private key?
if this is done, the file cannot be decrypted by A's public key anymore.  
if ppl decrypt the file using the malicious node's public address, then it no longer represents that it is a request from A.

okay, next is for the nodes to verify.
the basic verification is logically easy.
as this BTC to be sent can be traced all the way to its creation, the verification nodes just have to trace all the way to see if A really has this BTC.

why do they know the full history?
because each node has kept a copy of the full history of every single BTC's transactions.

btw every time we want to know how many BTC a public address (wallet) owns, it is always to look at the full history that has something to do with this address
and deduce the amount this address has.  
sounds efficient but it is always correct.

wait, if the verification is so easy, then whose node's verification is accepted?  
one important thing here is that to make sure the node realy puts efforts into verification,
the protocol artificially introduces some hard works for them to do.  
if a malicious node wants to approve a malicous transmit request, he can do but he still has to finish this artificial works.  
this is a concept of proof of work.

one example is that if we require each email sender to compute a hash value for the email he wants to send,
the spammers will have to spent a lot of resources if they want to spam a lot of receivers, which reduce their incentive to do so.

in BTC's case, the works required is to find a number (nouce) such that the hash value of the request file A sends and this number has to have enough leading 0s.
this work cannot be solved by any short cut except brute force.
whoever that is able to come out with a such a number will be the node that POTENTIALLY to the ONLY verifier that all other nodes recognize for this round.

in a simple scenario, if a node comes out with this number much faster than others, it will immediateely broadcast this verification to all other nodes.  
the finding of the number is every difficult, but the verification is very easy.
other nodes will verify if this node really achives this. if yes, they accept the answer and give up this own trial.
at this point, all nodes update their local copy of the full history of BTC.

what do you mean by "update the history of BTC"?
actullay the history is maintained by a blockchain.
in a blockchain, one block consists of its own information, plus a hash value of the previous block, plus a hash value of all the content. 

once a verification is accepted by a node, it add this block to the blockchain.

one simplification in the above example is that the node only verifies the transaction from A to B.
but in reality, serveral unverified transactions are grouped together and verified by a node.
therefore one block in blockchain is for verification of several transactions (in BTC).  
of course it doesn't prevent another design to approve one transaction at a time, but it will be extremely inefficient.

on the other hand, why not group even more transactions to one block?
the problem with a too big block is that a more powerful machine will tend to beat a less powerful machine if a block is too big,
which defeats the purpose of decentralization.  
in fact this is a on-going argument inside BTC community.  
actually BTC has been forked to form BCH, which has a bigger block (ultimately benefit big miners more).

back to the verification process.
why miners want to help verify the transactions?  
because there are rewards.
the miner who is the first to solve the math problem and gets accepted by all other nodes will be rewarded with new BTC.  
the number of of BTC rewarded is halved every 4 years.

what if a malicious node deliberately rejects the new block?
firstly, he is free to reject but most others will accept anyway.
there is no way for the malicious node to make 51% other nodes to reject the correct block.

besides, if the malicious node really want to accept a false transaction, he has to come out with a number faster than the whole network.
this is to compete with the whole nework's resources, which he unlikely will win.

but let's say he really manages to come out with a number faster than others, so what?
he cannot modify the content of the request file.
if the content itself is malicious (coming form this miner itself), other nodes will reject the block anyway because the content inside is not consistent..

the most difficult scenario is that A sends the BTC to B, and then sends the same BTC to C.
if request 1 is received by one miner only and request 2 is received by 2nd miner only,
from each miner's point of view, the request is correct.

assume that both miners are equally fast and make their own blocks and then broadcast.
nearly miners will accept the answer if they only receive one block.
but at some point, some miners will receive 2 versions of the blockchain, one with a history of A sends to B and one with A sends to C.  
the miner just has to accept one of them.
the rule is to accept the blockchain with the longest blocks.  
the thing here is that one transaction is not more correct than the other, so anyone will do.
but the rule is to accept the longest blockchain because it is hardest to recreate the full blockchain
and therefore hardest for any attackers to fake the blockchain.

whichever transaction is accepted, only one spending from A will be recorded so there is no double-spending problem.

you may ask what if A wants to send it to B but accidentally sends again to C later, but the 2nd request turns out to be accepted by the network?
that's A's problem.
the network maintains one history only.

btw can one node change part of the history and convince all other nodes to accept the modified history?  
both are difficult.
to change a few blocks, you need to create the number for each block to fulfil the hash requirement, which is time-consuming.
though ultimately you may achieve it (after many years of computation maybe), then what?
you need to hack into 51% of nodes that change their blockchains.. quite impossible.

in fact, the double-spending problem seems the most difficult one to solve but BTC's proof of work (POW) manages to solve this.

one more thing is that if more and more nodes joining the mining process, doesn't it mean that the verification process gets faster and faster?

the answer is no. because the protocol adjust the difficulty level of the hasing requirements based on the number of miners.
if more miners, the difficulty level increases.
ultimately it maintains a same average rate of creation of a new block (one new block every 10 min).

why do they want this?
this is to make sure if there are more nodes, the security is higher, because each miner is competing with all the others on a more difficult problem.
and the chance that any miner can solve this problem drops.
