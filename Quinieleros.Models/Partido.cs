using System;
using Quinieleros.Ligas;

namespace Quinieleros.Models
{
	public class Partido
	{
		public DateTime Fecha { get; set; }
		public Ligas.EquipoBase Local{ get; set; }
		public Ligas.EquipoBase Visitante{ get; set; }
		public	Resultado resultado{ get; set; }
		public int GolesLocal{ get; set; }
		public int GolesVisitante{ get; set; }
	}
}

