var space = 1;
for (var r=7; r>=0; r--) {
  var col = "";
  for (var c=0; c<8; c++) { col += "<td class='grid' id='"+r+c+"' value='"+r+c+"' data-pos='"+space+"'></td>"; space++;}
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
    		$.get(
    			url="path",
    			data={start:pos[0],end:pos[1]}, 
    			success=function(data) {
       				parsed_data = JSON.parse(data)
       				$("#path").append("<p>Shortest Path of Knight</p>")
       				for (cnt = 0; cnt < parsed_data.length; cnt++) {
       					id = String(parsed_data[cnt])
       					id = id.replace(/,/g, "");
       					$('#'+id).addClass("red");
       					console.log(id)
  						$("#path").append("<li>"+parsed_data[cnt]+"</li>");
					}
    			}
			);
    	}
	}
    
    // console.log(count)
    // console.log(pos)
})