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
    public partial class VerTiendas : Form
    {
        public VerTiendas()
        {
            InitializeComponent();
        }

        private void VerTiendas_Load(object sender, EventArgs e)
        {
            Conexion c = new Conexion();
            c.CargarTienda(dgvVerTiendas);
        }
    }
}
