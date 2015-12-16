using System;
using System.Collections.Generic;

namespace Quinieleros.Models
{
	public class Jornada
	{
		public string Nombre { get; set; }
		public List<Partido> partidos{ get; set; }
		public int Numero { get; set; }
	}
}

