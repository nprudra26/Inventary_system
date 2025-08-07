from flask import Flask, flash, render_template, request, redirect, url_for
from models import db, Employee
from datetime import datetime

from models.repair import Repair
from models.office_stationary import OfficeStationary

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        try:
            handover_date_str = request.form.get('handover_date')
            handover_date = datetime.strptime(handover_date_str, '%Y-%m-%d').date() if handover_date_str else None

            new_emp = Employee(
                emp_name=request.form['emp_name'],
                handover_date=handover_date,
                model_name=request.form.get('model_name'),
                laptop_name=request.form.get('laptop_name'),
                processor=request.form.get('processor'),
                windows=request.form.get('windows'),
                ssd=request.form.get('ssd'),
                ram=request.form.get('ram'),
                device_id=request.form.get('device_id'),
                product_serial_no=request.form.get('product_serial_no'),
                username=request.form.get('username'),
                hostname=request.form.get('hostname'),
                password=request.form.get('password'),
                dlp=request.form.get('dlp'),
                option_type=request.form.get('option_type', 'New')
            )

            db.session.add(new_emp)
            db.session.commit()
            return redirect(url_for('list_employees'))

        except Exception as e:
            return render_template('add_employee.html', error=str(e))

    return render_template('add_employee.html')

@app.route('/update-employee/<int:emp_id>', methods=['GET', 'POST'])
def update_employee(emp_id):
    employee = Employee.query.get_or_404(emp_id)

    if request.method == 'POST':
        try:
            employee.emp_name = request.form['emp_name']
            handover_date = request.form.get('handover_date')
            employee.handover_date = datetime.strptime(handover_date, '%Y-%m-%d').date() if handover_date else None
            employee.model_name = request.form.get('model_name')
            employee.laptop_name = request.form.get('laptop_name')
            employee.processor = request.form.get('processor')
            employee.windows = request.form.get('windows')
            employee.ssd = request.form.get('ssd')
            employee.ram = request.form.get('ram')
            employee.device_id = request.form.get('device_id')
            employee.product_serial_no = request.form.get('product_serial_no')
            employee.username = request.form.get('username')
            employee.hostname = request.form.get('hostname')
            employee.password = request.form.get('password')
            employee.dlp = request.form.get('dlp')
            employee.option_type = request.form.get('option_type')

            db.session.commit()
            return redirect(url_for('list_employees'))
        except Exception as e:
            return render_template('update_employee.html', employee=employee, error=str(e))

    return render_template('update_employee.html', employee=employee)

@app.route('/delete-employee/<int:emp_id>')
def delete_employee(emp_id):
    employee = Employee.query.get_or_404(emp_id)

    try:
        db.session.delete(employee)
        db.session.commit()
        return redirect(url_for('employee_list'))
    except Exception as e:
        return f"An error occurred while deleting: {str(e)}"

@app.route('/employees')
def employee_list():
    employees = Employee.query.all()
    return render_template('employee_list.html', employees=employees)


# Repair 
from datetime import datetime

@app.route('/add-repair', methods=['GET', 'POST'])
def add_repair():
    if request.method == 'POST':
        try:
            outward_date = datetime.strptime(request.form.get('outward_date'), '%Y-%m-%d').date()
            inward_str = request.form.get('inward_date')
            inward_date = datetime.strptime(inward_str, '%Y-%m-%d').date() if inward_str else None

            repair = Repair(
                device_type=request.form['device_type'],
                emp_name=request.form['emp_name'],
                device_id=request.form['device_id'],
                outward_date=outward_date,
                inward_date=inward_date,
                purpose_of_repair=request.form.get('purpose_of_repair'),
                client_name=request.form['client_name']
            )
            db.session.add(repair)
            db.session.commit()
            flash("Repair record added successfully.")
            return redirect(url_for('list_repairs'))

        except Exception as e:
            return render_template('add_repair.html', error=str(e))

    return render_template('add_repair.html')


@app.route('/update-repair/<int:repair_id>', methods=['GET', 'POST'])
def update_repair(repair_id):
    repair = Repair.query.get_or_404(repair_id)
    if request.method == 'POST':
        try:
            repair.device_type = request.form['device_type']
            repair.emp_name = request.form['emp_name']
            repair.device_id = request.form['device_id']
            repair.outward_date = datetime.strptime(request.form['outward_date'], '%Y-%m-%d').date()
            inward_str = request.form.get('inward_date')
            repair.inward_date = datetime.strptime(inward_str, '%Y-%m-%d').date() if inward_str else None
            repair.purpose_of_repair = request.form['purpose_of_repair']
            repair.client_name = request.form['client_name']
            
            db.session.commit()
            flash("Repair updated successfully.")
            return redirect(url_for('list_repairs'))
        except Exception as e:
            return render_template('update_repair.html', repair=repair, error=str(e))

    return render_template('update_repair.html', repair=repair)

@app.route('/delete-repair/<int:repair_id>')
def delete_repair(repair_id):
    repair = Repair.query.get_or_404(repair_id)
    try:
        db.session.delete(repair)
        db.session.commit()
        flash("Repair record deleted successfully.")
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')
    return redirect(url_for('list_repairs'))

@app.route('/repairs')
def repair_list():
    repairs = Repair.query.all()
    return render_template('repair_list.html', repairs=repairs)


# -------------------------------
# Office Stationary CRUD
# -------------------------------

@app.route('/add-stationary', methods=['GET', 'POST'])
def add_stationary():
    if request.method == 'POST':
        try:
            purchase_date = datetime.strptime(request.form['purchase_date'], '%Y-%m-%d').date()
            activation_date = datetime.strptime(request.form['activation_date'], '%Y-%m-%d').date()
            expiry_date = datetime.strptime(request.form['expiry_date'], '%Y-%m-%d').date()

            item = OfficeStationary(
                product_name=request.form['product_name'],
                mail_id=request.form['mail_id'],
                purchase_date=purchase_date,
                activation_date=activation_date,
                expiry_date=expiry_date,
                warranty_years=int(request.form['warranty_years']),
                make_in=request.form['make_in']
            )
            db.session.add(item)
            db.session.commit()
            flash("Stationary item added successfully.")
            return redirect(url_for('stationary_list'))
        except Exception as e:
            return render_template('add_stationary.html', error=str(e))

    return render_template('add_stationary.html')


@app.route('/update-stationary/<int:stationary_id>', methods=['GET', 'POST'])
def update_stationary(stationary_id):
    item = OfficeStationary.query.get_or_404(stationary_id)

    if request.method == 'POST':
        try:
            item.product_name = request.form['product_name']
            item.mail_id = request.form['mail_id']
            item.purchase_date = datetime.strptime(request.form['purchase_date'], '%Y-%m-%d').date()
            item.activation_date = datetime.strptime(request.form['activation_date'], '%Y-%m-%d').date()
            item.expiry_date = datetime.strptime(request.form['expiry_date'], '%Y-%m-%d').date()
            item.warranty_years = int(request.form['warranty_years'])
            item.make_in = request.form['make_in']

            db.session.commit()
            flash("Stationary item updated.")
            return redirect(url_for('stationary_list'))
        except Exception as e:
            return render_template('update_stationary.html', stationary=item, error=str(e))

    return render_template('update_stationary.html', stationary=item)


@app.route('/delete-stationary/<int:stationary_id>')
def delete_stationary(stationary_id):
    item = OfficeStationary.query.get_or_404(stationary_id)
    try:
        db.session.delete(item)
        db.session.commit()
        flash("Item deleted successfully.")
    except Exception as e:
        flash(f"Error: {str(e)}", 'error')
    return redirect(url_for('stationary_list'))


@app.route('/stationary')
def stationary_list():
    stationaries = OfficeStationary.query.all()
    return render_template('stationary_list.html', stationaries=stationaries)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
