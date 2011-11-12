<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"> 
<html lang="en"> 
<head> 
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"> 
  <title>DirShare</title>
  <link rel="stylesheet" href="/static/style.css" type="text/css"/>
</head>
<body>
  </form>
	<div class="content">
		<div class="path">
				<INPUT TYPE="button" VALUE="<<--" onClick="history.go(-1)"> <INPUT TYPE="button" VALUE="-->>" onClick="history.go(1)"> PATH: {{ path_dir }}
		</div>
		<table id="fileTable">
			<thead>
				<tr>
					<th>Name</th>
					<th>Date</th>
					<th>Size</th>
				</tr>
			</thead>
			<tbody>
				% for item in to_html_1:
				 <tr><td><i class='icon folder'></i><a href='{{ item[0] }}/{{ item[1] }}'>{{ item[2] }} </a></td> <td class='data'>{{ item[3] }}</td> <td class='data'>{{ item[4] }}</td> </tr>
				% end
				% for item in to_html_2:
				 <tr><td><i class='icon {{ item[0] }}'></i><a href='/download?file={{ item[1] }}/{{ item[2] }}'>{{ item[3] }}</a></td> <td class='data'>{{ item[4] }}</td> <td class='data'>{{ item[5] }}</td> </tr>
				% end
			</tbody>
		</table>
		<div class="footer"></div>
	</div>
</body>
</html>*
