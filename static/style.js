var space = 1;
for (var r=7; r>=0; r--) {
  var col = "";
  for (var c=0; c<8; c++) { col += "<td class='grid' value='("+r+","+c+")' data-pos='"+space+"'></td>"; space++;}
  $("#chessboard").append("<tr>"+col+"</tr>");
}
var count = 0
var pos = []
$('.grid').click(function(){
	if(count<2){
		$(this).addClass("clicked");
    	pos.push($(this).attr('value'))
    	count++;
    	if(count==2){
    		$("#chessboard").attr("disabled","disabled").css("cursor", "default")
    	}
	}
    
    console.log(count)
    console.log(pos)
})