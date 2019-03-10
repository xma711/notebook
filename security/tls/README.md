Transport Layer Security (TLS)
-----------------------------------

Reference: https://www.networkworld.com/article/2303073/lan-wan/lan-wan-what-is-transport-layer-security-protocol.html

"TLS is a cryptographic protocol that provides end-to-end communications security over networks."

TLS "defines two layers.
The TLS record protocol provides connection security,
and the TLS handshake protocol enables the client and server to authenticate each other
and to negotiate security keys before any data is transmitted."

"A basic TLS handshake involves the client and server sending hello messages,
and the exchange of keys,
cipher message and a finish message".

The handshake process can be viewed in diagram in https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_7.1.0/com.ibm.mq.doc/sy10660_.htm

How TLS provides authentication: https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_7.1.0/com.ibm.mq.doc/sy10670_.htm


X.509
--------------------

Reference: https://en.wikipedia.org/wiki/X.509

"An x.509 certificate contains a public key and an identity...,
and is either signed by a certificate authority or self-signed.
When a certificates is signed by a trusted certificate authority...,
someone holding that certificate can rely on the public key it contains to
establish secure communications with another party,
or validate documents digitally signed by the corresponding private key."
