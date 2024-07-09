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
    public partial class Form2 : Form
    {
        Conexion c = new Conexion();
        public Form2()
        {
            InitializeComponent();
        }

        private void btnRegistrar_Click(object sender, EventArgs e)
        {
            if (c.registradoProducto(Convert.ToInt32(txtProducto.Text)) == 0)
            {
                c.insertarProducto(Convert.ToInt32(txtProducto.Text), txtCategoria.Text, Convert.ToInt32(txtExistencia.Text), txtMarca.Text, Convert.ToInt32(txtPrecio.Text),Convert.ToInt32(txtTamano.Text), txtFecha.Text, Convert.ToInt32(txtTienda.Text));
                MessageBox.Show("Registro ingresado");
                txtProducto.Text = "";
                txtCategoria.Text = "";
                txtExistencia.Text = "";
                txtMarca.Text = "";
                txtPrecio.Text = "";
                txtTamano.Text = "";
                txtFecha.Text = "";
                txtTienda.Text = "";

            }
            else 
            {
                MessageBox.Show("No se pudo realizar el registro");
            }

        }

        private void btnVer_Click(object sender, EventArgs e)
        {
            Form FormularioVer = new VerProducto();
            FormularioVer.Show();
        }

        private void btnModificar_Click(object sender, EventArgs e)
        {
            MessageBox.Show(c.ModificarProducto(Convert.ToInt32(txtPrecio.Text), txtCategoria.Text, Convert.ToInt32(txtExistencia.Text), txtMarca.Text, Convert.ToInt32(txtPrecio.Text), Convert.ToInt32(txtTamano.Text), txtFecha.Text, Convert.ToInt32(txtTienda.Text)));
        }

        private void btnBuscar_Click(object sender, EventArgs e)
        {
            if (c.registradoProducto(Convert.ToInt32(txtProducto.Text)) > 0)
            {
                c.BusquedaProducto(Convert.ToInt32(txtProducto.Text), txtCategoria, txtExistencia, txtMarca, txtPrecio, txtTamano, txtFecha, txtTienda);
            }
            else
            {
                txtProducto.Text = "";
                txtCategoria.Text = "";
                txtExistencia.Text = "";
                txtMarca.Text = "";
                txtPrecio.Text = "";
                txtTamano.Text = "";
                txtFecha.Text = "";
                txtTienda.Text = "";
            }
        }

        private void btnEliminar_Click(object sender, EventArgs e)
        {
            if (c.registradoProducto(Convert.ToInt32(txtProducto.Text)) > 0)
            {
                c.eliminarProducto(Convert.ToInt32(txtProducto.Text), txtCategoria, txtExistencia, txtMarca, txtPrecio, txtTamano, txtFecha, txtTienda);
                txtProducto.Text = "";
                txtCategoria.Text = "";
                txtExistencia.Text = "";
                txtMarca.Text = "";
                txtPrecio.Text = "";
                txtTamano.Text = "";
                txtFecha.Text = "";
                txtTienda.Text = "";
            }
            else
            {
                MessageBox.Show("No se ha podido eliminar el producto");
            }
        }
    }
}
