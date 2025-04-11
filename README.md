# Local PoC

#### Purpose

Ensure Traefik works correctly on a non-corporate setup using Docker

- [http://localhost:8080/](http://localhost:8080/) should open Traefik dashboard
- [http://localhost/whoami](http://localhost/whoami) should redirect to whoami
- [http://localhost:8081/](http://localhost:8081/) should directly open helloworld
- [http://helloworld.localhost/](http://helloworld.localhost/) should redirect to helloworld
- [http://localhost/helloworld](http://localhost/helloworld) idem (FAILED)
