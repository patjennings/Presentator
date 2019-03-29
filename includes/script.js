let cursor = 0;
let elements;
let offsets = [];
document.addEventListener("DOMContentLoaded", function(event){
    startPresentation();
});

function startPresentation(){
    elements = document.getElementsByTagName("section");

    for(i=0 ; i<elements.length; i++){
	var pos = offset(elements[i]).top;
	offsets.push(pos);
    }
    
    document.body.onclick = function(event){
	if(cursor < elements.length-1){
	    cursor+=1;
	    this.scrollTop = offsets[cursor];
	} else {
	    console.log("fin de la présentation")
	}
    }
    document.body.onscroll = function(event){
	bodypos = document.body.scrollTop
	if(bodypos < offsets[cursor]-20){
	    cursor-=1;
	}
    }
}

// fonction qui permet de placer / équivalent de jQuery offset() 
function offset(elt) {
    var rect = elt.getBoundingClientRect(), bodyElt = document.body;
    return {
	top: rect.top + bodyElt .scrollTop,
	left: rect.left + bodyElt .scrollLeft
    }
}
