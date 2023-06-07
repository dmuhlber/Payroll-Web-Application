import sqlite3
from bottle import route, run, request, template

@route('/', method='GET')
def index():
    data = {'title': 'Welcome!'} 
    return template('welcome', data)

@route('/getDepartment', method = ['GET', 'POST'])
def department():

    if request.method == 'GET':
        return template('dept_form')
    else:
        dept = request.forms.get("dept")
        conn = sqlite3.connect("payroll.db")
        cur = conn.cursor()

        sql = '''SELECT pay_data.emp_id, emp_name, wage, hrs_worked FROM employees
                JOIN pay_data
                WHERE pay_data.emp_id = employees.emp_id AND employees.department = ?'''
        cur.execute(sql, (dept,))

        rows = cur.fetchall()
        cur.close()
        hrs = 0
        wage = 0

        if rows:

            dataList = []
            for row in rows:
                eid, name, wage, hrs = row
                if hrs <= 40:
                    payout = wage * hrs
                else:
                    ot_pay = (hrs - 40) * 1.5 * wage
                    payout = (wage * 40) + ot_pay

                emp = (eid, name, wage, hrs, payout)
                dataList.append(emp)

            data = {'rows': dataList, 'dept': dept}
            return template('show_department', data)
        
        else:
            msg = 'no such username'


@route('/editHours', method = ['GET', 'POST'])
def edit_hrs():
    if request.method == 'GET':
        return template('edit_hours')
    else:
        hrs = request.forms.get('hrs')
        eid = request.forms.get('eid')

        try:
            conn = sqlite3.connect("payroll.db")
            cur = conn.cursor()

            sql = '''SELECT employees.emp_id, emp_name, department, pay_period FROM employees
                    JOIN employees
                    WHERE employees.emp_id = pay_data.emp_id AND employees.department = ?'''
            cur.execute(sql, (hrs, eid))
            result = cur.fetchone()

            if result:
                data = {'rows': result}
                return template('status')

        except sqlite3.Error as er:
            msg = {'op': 'SELECT', 'status': 'unsuccessful'}
        
            print('SQLite error: %s' % (' '.join(er.args)))
            return template('status', msg)  # status page: success or no-success
        
        finally:
            c.close()
                

        
 
run(host='localhost', port=8080) 
    
