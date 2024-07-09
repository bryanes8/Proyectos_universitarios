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
    public partial class Tiendas : Form
    {
        Conexion c = new Conexion();
        public Tiendas()
        {
            InitializeComponent();
        }

        private void btnVer_Click(object sender, EventArgs e)
        {
            Form FormularioVer = new VerTiendas();
            FormularioVer.Show();
        }

        private void btnModificar_Click(object sender, EventArgs e)
        {
            MessageBox.Show(c.ModificarTienda(Convert.ToInt32(txtTienda.Text), txtMunicipio.Text, txtDepartamento.Text, txtDireccion.Text, txtEncargado.Text, Convert.ToInt32(txtTelefono.Text)));
        }

        private void btnBuscar_Click(object sender, EventArgs e)
        {
            if (c.registradoTienda(Convert.ToInt32(txtTienda.Text)) > 0)
            {
                c.BusquedaTienda(Convert.ToInt32(txtTienda.Text), txtMunicipio, txtDepartamento, txtDireccion, txtEncargado, txtTelefono);
            }
            else
            {
                txtTienda.Text = "";
                txtMunicipio.Text = "";
                txtDepartamento.Text = "";
                txtDireccion.Text = "";
                txtEncargado.Text = "";
                txtTelefono.Text = "";
            }
        }

        private void btnCargar_Click(object sender, EventArgs e)
        {

        }
    }
}


