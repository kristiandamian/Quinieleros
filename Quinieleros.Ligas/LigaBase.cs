using System;
using System.Collections.Generic;

namespace Quinieleros.Ligas
{
	public abstract class LigaBase
	{
		public string NombreLiga { get; set; }
        public string ClaveLiga { get; set; }
        public string Pais { get; set; }
		public List<EquipoBase> Equipos { get; set; }
	}
}

