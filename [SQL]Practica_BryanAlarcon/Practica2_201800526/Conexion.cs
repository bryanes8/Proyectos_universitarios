using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.Sql;
using System.Data.SqlClient;
using System.Windows.Forms;

namespace Practica2_201800526
{
    class Conexion
    {
        SqlConnection cn;
        SqlCommand cmd;
        SqlDataReader dr;
        SqlDataAdapter da;
        DataTable dt;

        public Conexion()
        {
            try
            {
                cn = new SqlConnection("Data Source=.;Initial Catalog=Practica2_201800526;Integrated Security=True");
                cn.Open();
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se pudo conectar con la base de datos: " + ex.ToString());
            }
        }
        public string insertarProducto(int idProducto, string categoria, int existencia, string marca, float precio, float Tamano, string fecha, int tienda)
        {
            string salida = "Si se inserto";

            try
            {
                cmd = new SqlCommand("Insert into Producto(id_Producto,Categoria,Existencias,Marca,Precio,tamanio,Fecha_vencimiento,id_Tiendas) values(" + idProducto + ",'" + categoria + "'," + existencia + ",'" + marca + "'," + precio + "," + Tamano + ",'" + fecha + "'," + tienda + ")", cn);
                cmd.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                salida = "No se conecto: " + ex.ToString();
            }
            return salida;
        }

        public int registradoProducto(int idProducto)
        {
            int contador = 0;

            try
            {
                cmd = new SqlCommand("Select * from Producto where id_Producto=" + idProducto + "", cn);
                dr = cmd.ExecuteReader();
                while (dr.Read())
                {
                    contador++;
                }
                dr.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se pudo encontrar el valor");
            }
            return contador;
        }
        public void CargarProducto(DataGridView dgv)
        {
            try
            {
                da = new SqlDataAdapter("Select * from Producto", cn);
                dt = new DataTable();
                da.Fill(dt);
                dgv.DataSource = dt;
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se pudo llenar el DatagridView: " + ex.ToString());
            }
        }
        public void BusquedaProducto(int idProducto, TextBox txtCategoria, TextBox txtExistencia, TextBox txtMarca, TextBox txtPrecio, TextBox txtTamano, TextBox txtFecha, TextBox txtTienda)
        {
            try
            {
                cmd = new SqlCommand("Select * from Producto where id_Producto=" + idProducto + "", cn);
                dr = cmd.ExecuteReader();
                if (dr.Read())
                {
                    txtCategoria.Text = dr["Categoria"].ToString();
                    txtExistencia.Text = dr["Existencias"].ToString();
                    txtMarca.Text = dr["Marca"].ToString();
                    txtPrecio.Text = dr["Precio"].ToString();
                    txtTamano.Text = dr["tamanio"].ToString();
                    txtFecha.Text = dr["Fecha_vencimiento"].ToString();
                    txtTienda.Text = dr["id_Tiendas"].ToString();
                }
                dr.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se pudieron llenar los campos: " + ex.ToString());
            }
        }
        public string ModificarProducto(int idProducto, string categoria, int existencia, string marca, float precio, float Tamano, string fecha, int tienda)
        {
            string salida = "Se actualizaron los datos";
            try
            {
                cmd = new SqlCommand("Update Producto set Categoria='" + categoria + "' ,Existencias= " + existencia + " ,Marca ='" + marca + "' ,Precio =" + precio + " ,tamanio= " + Tamano + " ,Fecha_vencimiento= '" + fecha + "' ,id_Tiendas= " + tienda + " where id_Producto= " + idProducto + "", cn);
                cmd.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                salida = "No se actualizo " + ex.ToString();
            }
            return salida;
        }
        public int eliminarProducto(int idProducto, TextBox txtCategoria, TextBox txtExistencia, TextBox txtMarca, TextBox txtPrecio, TextBox txtTamano, TextBox txtFecha, TextBox txtTienda)
        {
            int contador = 0;

            try
            {
                cmd = new SqlCommand("DELETE FROM Producto WHERE id_Producto=" + idProducto + "", cn);
                dr = cmd.ExecuteReader();
                MessageBox.Show("El producto se ha eliminado");
                while (dr.Read())
                {
                    contador++;
                }
                dr.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se ha podido eliminar el producto");
            }
            return contador;
        }





        public void CargarEmpleado(DataGridView dgv)
        {
            try
            {
                da = new SqlDataAdapter("Select * from Empleados", cn);
                dt = new DataTable();
                da.Fill(dt);
                dgv.DataSource = dt;
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se pudo llenar el DatagridView: " + ex.ToString());
            }
        }
        public string insertarEmpleado(int idEmpleado, string nombre, string apellido, int telefono, string puesto, string fechainicio, string fechafin, string horainicio, string horafinal, int tienda, string jefe, string contrasena)
        {
            string salida = "Si se inserto";

            try
            {
                cmd = new SqlCommand("Insert into Empleados(CUI,Nombre,Apellido,Telefono,Puesto,Fecha_inicio,Fecha_fin,Hora_inicio,Hora_fin,id_Tiendas,Jefe,Password) values(" + idEmpleado + ",'" + nombre + "','" + apellido + "'," + telefono + ",'" + puesto + "','" + fechainicio + "','" + fechafin + "','" + horainicio + "','" + horafinal + "'," + tienda + ",'" + jefe + "','" + contrasena + "')", cn);
                cmd.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                salida = "No se conecto: " + ex.ToString();
            }
            return salida;
        }
        public int registradoEmpleado(int idEmpleado)
        {
            int contador = 0;

            try
            {
                cmd = new SqlCommand("Select * from Empleados where CUI=" + idEmpleado + "", cn);
                dr = cmd.ExecuteReader();
                while (dr.Read())
                {
                    contador++;
                }
                dr.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se pudo encontrar el valor");
            }
            return contador;
        }
        public void BusquedaEmpleado(int idEmpleado, TextBox txtNombre, TextBox txtApellido, TextBox txtTelefono, TextBox txtPuesto, TextBox txtFechaInicio, TextBox txtFechaFin, TextBox txtHoraInicio, TextBox txtHoraFin,TextBox txtTienda, TextBox txtJefe, TextBox txtContrasena)
        {
            try
            {
                cmd = new SqlCommand("Select * from Empleados where CUI=" + idEmpleado + "", cn);
                dr = cmd.ExecuteReader();
                if (dr.Read())
                {
                    txtNombre.Text = dr["Nombre"].ToString();
                    txtApellido.Text = dr["Apellido"].ToString();
                    txtTelefono.Text = dr["Telefono"].ToString();
                    txtPuesto.Text = dr["Puesto"].ToString();
                    txtFechaInicio.Text = dr["Fecha_inicio"].ToString();
                    txtFechaFin.Text = dr["Fecha_fin"].ToString();
                    txtHoraInicio.Text = dr["Hora_inicio"].ToString();
                    txtHoraFin.Text = dr["Hora_fin"].ToString();
                    txtTienda.Text = dr["id_Tiendas"].ToString();
                    txtJefe.Text = dr["Jefe"].ToString();
                    txtContrasena.Text = dr["Password"].ToString();
                }
                dr.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se pudieron llenar los campos: " + ex.ToString());
            }
        }
        public string ModificarEmpleado(int idEmpleado, string nombre, string apellido, int telefono, string puesto, string fechainicio, string fechafin, string horainicio, string horafinal, int tienda, string jefe, string contrasena)
        {
            string salida = "Se actualizaron los datos";
            try
            {
                cmd = new SqlCommand("Update Empleados set Nombre='" + nombre + "' ,Apellido= '" + apellido + "' ,Telefono =" + telefono + " ,Puesto ='" + puesto + "' ,Fecha_inicio= '" + fechainicio + "' ,Fecha_fin= '" + fechafin + "' ,Hora_inicio= '" + horainicio + "' ,Hora_fin= '" + horafinal + "',id_Tiendas= " + tienda + " ,Jefe= '" + jefe + "' ,Password= '" + contrasena + "'where CUI= " + idEmpleado + "", cn);
                cmd.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                salida = "No se actualizo " + ex.ToString();
            }
            return salida;
        }
        public int eliminarEmpleado(int idEmpleado, TextBox txtNombre, TextBox txtApellido, TextBox txtTelefono, TextBox txtPuesto, TextBox txtFechaInicio, TextBox txtFechaFin, TextBox txtHoraInicio, TextBox txtHoraFin, TextBox txtTienda, TextBox txtJefe, TextBox txtContrasena)
        {
            int contador = 0;

            try
            {
                cmd = new SqlCommand("DELETE FROM Empleados WHERE CUI=" + idEmpleado + "", cn);
                dr = cmd.ExecuteReader();
                MessageBox.Show("El empleado se ha eliminado");
                while (dr.Read())
                {
                    contador++;
                }
                dr.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se ha podido eliminar el empleado");
            }
            return contador;
        }





        public void CargarTienda(DataGridView dgv)
        {
            try
            {
                da = new SqlDataAdapter("Select * from Tiendas", cn);
                dt = new DataTable();
                da.Fill(dt);
                dgv.DataSource = dt;
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se pudo llenar el DatagridView: " + ex.ToString());
            }
        }
        public int registradoTienda(int idTienda)
        {
            int contador = 0;

            try
            {
                cmd = new SqlCommand("Select * from Tiendas where id_Tiendas=" + idTienda + "", cn);
                dr = cmd.ExecuteReader();
                while (dr.Read())
                {
                    contador++;
                }
                dr.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se pudo encontrar el valor");
            }
            return contador;
        }
        public void BusquedaTienda(int idTienda, TextBox txtMunicipio, TextBox txtDepartamento, TextBox txtDireccion, TextBox txtEncargado, TextBox txtTelefono)
        {
            try
            {
                cmd = new SqlCommand("Select * from Tiendas where id_Tiendas=" + idTienda + "", cn);
                dr = cmd.ExecuteReader();
                if (dr.Read())
                {
                    txtMunicipio.Text = dr["Municipio"].ToString();
                    txtDepartamento.Text = dr["Departamento"].ToString();
                    txtDireccion.Text = dr["Direccion"].ToString();
                    txtEncargado.Text = dr["Encargado"].ToString();
                    txtTelefono.Text = dr["Telefono"].ToString();
                }
                dr.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se pudieron llenar los campos: " + ex.ToString());
            }
        }
        public string ModificarTienda(int idTienda, string municipio, string departamento, string direccion, string encargado, int telefono)
        {
            string salida = "Se actualizaron los datos";
            try
            {
                cmd = new SqlCommand("Update Tiendas set Municipio='" + municipio + "' ,Departamento= '" + departamento + "' ,Direccion ='" + direccion + "' ,Encargado ='" + encargado + "' ,Telefono= " + telefono + "where id_Tiendas= " + idTienda + "", cn);
                cmd.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                salida = "No se actualizo " + ex.ToString();
            }
            return salida;
        }

    }
}
