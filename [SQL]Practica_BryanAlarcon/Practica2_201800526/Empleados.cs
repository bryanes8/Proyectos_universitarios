using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Practica2_201800526
{
    public partial class Empleados : Form
    {
        Conexion c = new Conexion();
        public Empleados()
        {
            InitializeComponent();
        }

        private void btnVer_Click(object sender, EventArgs e)
        {
            Form FormularioVer = new VerEmpleados();
            FormularioVer.Show();
        }

        private void btnRegistro_Click(object sender, EventArgs e)
        {
            if (c.registradoEmpleado(Convert.ToInt32(txtCUI.Text)) == 0)
            {
                c.insertarEmpleado(Convert.ToInt32(txtCUI.Text), txtNombre.Text,txtApellido.Text, Convert.ToInt32(txtTelefono.Text), txtPuesto.Text, txtFechaIni.Text, txtFechaFin.Text, txtHoraIni.Text, txtHoraFin.Text, Convert.ToInt32(txtTienda.Text), txtJefe.Text, txtPassword.Text);
                MessageBox.Show("Registro ingresado");
                txtCUI.Text = "";
                txtNombre.Text = "";
                txtApellido.Text = "";
                txtTelefono.Text = "";
                txtPuesto.Text = "";
                txtFechaIni.Text = "";
                txtFechaFin.Text = "";
                txtHoraIni.Text = "";
                txtHoraFin.Text = "";
                txtTienda.Text = "";
                txtJefe.Text = "";
                txtPassword.Text = "";

            }
            else
            {
                MessageBox.Show("No se pudo realizar el registro");
            }
        }

        private void btnBuscar_Click(object sender, EventArgs e)
        {
            if (c.registradoEmpleado(Convert.ToInt32(txtCUI.Text)) > 0)
            {
                c.BusquedaEmpleado(Convert.ToInt32(txtCUI.Text), txtNombre, txtApellido, txtTelefono, txtPuesto, txtFechaIni, txtFechaFin, txtHoraIni, txtHoraFin, txtTienda, txtJefe, txtPassword);
            }
            else
            {
                txtCUI.Text = "";
                txtNombre.Text = "";
                txtApellido.Text = "";
                txtTelefono.Text = "";
                txtPuesto.Text = "";
                txtFechaIni.Text = "";
                txtFechaFin.Text = "";
                txtHoraIni.Text = "";
                txtHoraFin.Text = "";
                txtTienda.Text = "";
                txtJefe.Text = "";
                txtPassword.Text = "";
            }
        }

        private void btnModificar_Click(object sender, EventArgs e)
        {
            MessageBox.Show(c.ModificarEmpleado(Convert.ToInt32(txtCUI.Text), txtNombre.Text, txtApellido.Text, Convert.ToInt32(txtTelefono.Text), txtPuesto.Text, txtFechaIni.Text, txtFechaFin.Text, txtHoraIni.Text, txtHoraFin.Text, Convert.ToInt32(txtTienda.Text), txtJefe.Text, txtPassword.Text));
        }

        private void btnEliminar_Click(object sender, EventArgs e)
        {
            if (c.registradoEmpleado(Convert.ToInt32(txtCUI.Text)) > 0)
            {
                c.eliminarEmpleado(Convert.ToInt32(txtCUI.Text), txtNombre, txtApellido, txtTelefono, txtPuesto, txtFechaIni, txtFechaFin, txtHoraIni, txtHoraFin, txtTienda, txtJefe, txtPassword);
                txtCUI.Text = "";
                txtNombre.Text = "";
                txtApellido.Text = "";
                txtTelefono.Text = "";
                txtPuesto.Text = "";
                txtFechaIni.Text = "";
                txtFechaFin.Text = "";
                txtHoraIni.Text = "";
                txtHoraFin.Text = "";
                txtTienda.Text = "";
                txtJefe.Text = "";
                txtPassword.Text = "";
            }
            else
            {
                MessageBox.Show("No se ha podido eliminar el empleado");
            }
        }
    }
    
}
