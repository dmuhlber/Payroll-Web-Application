% rebase('layout.tpl', title='department')
 
	
		<h4>Get Payroll by Department<h4>
		<br>
		<p>
		<form method='post' action='/getDepartment'>
		
		   Select Department: <select name='department'>
		       <option value='1'>advertising</option>
			   <option value='2'>maintenance</option>
			   <option value='3'>environment</option>
			   <option value='4'>shipping</option>
		    </select> &nbsp; 
			
			<input type='Submit'>
		<form>
		</p>
    <br>
