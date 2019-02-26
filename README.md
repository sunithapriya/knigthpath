# Shortest Knight path between source and destination

Implemeted Using python and Flask.

**Implemented Tasks**:
* Created an html page with a chessboard (8x8 grid).  
Numbers 0-7 represent the corresponging rows and columns. For example (7,0) represents the top left grid 
<img width="544" alt="screen shot 2019-02-26 at 12 11 34 am" src="https://user-images.githubusercontent.com/43215312/53389542-b43ab980-395d-11e9-85f8-572600721b6f.png">

* User can select any two grids (one source, one destination - indicated by the green grids below). 
An ajax call is made after the destination grid is selected. 
The shortest path is then calculated using the api(pathapi.py) 
The json output returned by the api is then displayed on the page. The path is also indicated by the grids highlighted with red border.
<img width="925" alt="screen shot 2019-02-26 at 12 12 00 am" src="https://user-images.githubusercontent.com/43215312/53389665-2a3f2080-395e-11e9-8140-e15c5c0262a9.png">

**Steps to run the code**:
* Install the requirements <br>
```pip install requirements.txt```
* Run main.py <br>
```python main.py``` <br>
It should display an output as below:
<img width="551" alt="screen shot 2019-02-26 at 12 40 37 am" src="https://user-images.githubusercontent.com/43215312/53389951-6626b580-395f-11e9-801c-18e5900830d2.png">

Load the url (http://127.0.0.1:5000/) into a web browser. <br>
Click any two grids to detemine the path between them.
