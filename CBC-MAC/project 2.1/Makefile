cbc-encrypt: aes_core.o cbc-encrypt.o
	gcc -o cbc-encrypt cbc-encrypt.o aes_core.o; rm cbc-encrypt.o

cbc-encrypt.o:
	gcc -c cbc-encrypt.c

aes_core.o:
	gcc -c aes_core.c

clean:
	rm -rf *.o sample
