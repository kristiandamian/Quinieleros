using System;
using System.Collections.Generic;


namespace Quinieleros.Models
{
	public class Calendario
	{
		public string Nombre { get; set; }
		public List<Jornada> Jornadas{ get; set; }
		public DateTime FechaInicio { get; set; }
		public DateTime FechaFin { get; set; }
		public Ligas.LigaBase Liga { get; set; }
	}
}

